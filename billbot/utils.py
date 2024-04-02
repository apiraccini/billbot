# utils.py
"""Module for managing document indexing and retrieval."""

from pathlib import Path
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

from llama_index.core import VectorStoreIndex, get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

from dotenv import load_dotenv

def initialize_settings():
    """
    Initialize settings for document parsing and indexing.
    """
    # load environment variables
    load_dotenv()

    # llm settings
    Settings.llm = OpenAI(model='gpt-3.5-turbo', temperature=0.1)
    Settings.embed_model = OpenAIEmbedding(model='text-embedding-ada-002')

    # document parsing settings
    Settings.chunk_size = 512
    Settings.chunk_overlap = 20


def get_index(persist_dir: Path, raw_data_dir: Path) -> VectorStoreIndex:
    """
    Retrieve or create a document index.

    args:
        persist_dir (Path): Directory for persisting the index.
        raw_data_dir (Path): Directory containing raw data for indexing.

    returns:
        VectorStoreIndex: The document index.
    """
    initialize_settings()

    if not persist_dir.exists():
        parser = LlamaParse(result_type='markdown', verbose=True)
        file_extractor = {'.pdf': parser}
        documents = SimpleDirectoryReader(raw_data_dir, file_extractor=file_extractor, recursive=True).load_data()
        index = VectorStoreIndex.from_documents(documents, show_progress=True)

        persist_dir.mkdir(exist_ok=True)
        index.storage_context.persist(persist_dir=persist_dir)
    else:
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context=storage_context)

    return index


def get_query_engine(index: VectorStoreIndex) -> RetrieverQueryEngine:
    """
    Create and configure a query engine for the given document index.

    Args:
        index (VectorStoreIndex): The document index.

    Returns:
        RetrieverQueryEngine: The configured query engine.
    """
    # configure retriever
    retriever = VectorIndexRetriever(
        index=index,
        similarity_top_k=5,
    )

    # configure response synthesizer
    response_synthesizer = get_response_synthesizer(response_mode='compact')

    # configure node postprocessors
    node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)]

    # assemble query engine
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer,
        node_postprocessors=node_postprocessors,
    )

    return query_engine