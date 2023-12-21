import chromadb
from chromadb.config import Settings

chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="hackathon-2023/bdd/"))
# collection permet de stocker embeddings, documents et autre metadata
collection = chroma_client.get_or_create_collection(name="article")

result = collection.get(ids="1")

print(result)