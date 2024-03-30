from pathlib import Path

from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

from dotenv import load_dotenv
load_dotenv()

raw_data_dir = Path('./data')
persist_dir = Path('./storage')

def get_index(persist_dir, raw_data_dir):

    if not persist_dir.exists():

        parser = LlamaParse(result_type='markdown', verbose=True)
        file_extractor = {'.pdf': parser}

        documents = SimpleDirectoryReader(raw_data_dir, file_extractor=file_extractor).load_data()
        index = VectorStoreIndex.from_documents(documents)

        persist_dir.mkdir(exist_ok=True)
        index.storage_context.persist(persist_dir=persist_dir)

    else:
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)

    return index