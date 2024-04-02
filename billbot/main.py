# main.py
from pathlib import Path
from utils import get_index, get_query_engine

def main(query: str, persist_dir: Path, raw_data_dir: Path) -> str:
    """
    Main function to query documents based on the input query.

    args:
        query (str): The query string.
        persist_dir (Path): Directory for persisting the index.
        raw_data_dir (Path): Directory containing raw data for indexing.

    returns:
        str: The response to the query.
    """
    # retrieve or create the document index and get query engine
    index = get_index(persist_dir=persist_dir, raw_data_dir=raw_data_dir)
    query_engine = get_query_engine(index)
    
    # get response
    response = query_engine.query(query)
    
    return response


if __name__ == "__main__":

    # directories
    raw_data_dir = Path('./data')
    persist_dir = Path('./storage')

    # example query
    query = "Fammi un resoconto delle ultime bollette che ho pagato per i vari servizi."

    # execute the main function and print the response
    response = main(query=query, persist_dir=persist_dir, raw_data_dir=raw_data_dir)
    print(response)