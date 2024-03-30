from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage

from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

raw_data_dir = Path('./data')
presist_dir = Path('./storage')

def get_index(storage_path, raw_data_path):

    if not storage_path.exists():

        parser = LlamaParse(result_type='markdown', verbose=True)
        file_extractor = {'.pdf': parser}

        documents = SimpleDirectoryReader(raw_data_path, file_extractor=file_extractor).load_data()
        index = VectorStoreIndex.from_documents(documents)

        storage_path.mkdir(exist_ok=True)
        index.storage_context.persist(persist_dir=presist_dir)

    else:
        storage_context = StorageContext.from_defaults(persist_dir=presist_dir)
        index = load_index_from_storage(storage_context)

    return index