from pathlib import Path
from utils import get_index
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# define llm settings
embed_model=OpenAIEmbedding(model="text-embedding-3-small")
llm = OpenAI(model="gpt-3.5-turbo-0125")

Settings.llm = llm
Settings.embed_model = embed_model

raw_data_dir = Path('./data')
persist_dir = Path('./storage')

# example query
query = "Fammi un resoconto della mia situazione per quanto rigurarda le bollette tari (totale pagato, periodo di riferimento)"

index = get_index(persist_dir=persist_dir, raw_data_dir=raw_data_dir)
query_engine = index.as_query_engine()
response = query_engine.query(query)

print(response)