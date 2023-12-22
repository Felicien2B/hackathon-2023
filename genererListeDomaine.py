import chromadb
from chromadb.config import Settings
import json
import numpy as np

chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="hackathon-2023/bdd/"))
# collection permet de stocker embeddings, documents et autre metadata
collection = chroma_client.get_or_create_collection(name="article")

result = collection.get()

list_domain = []

for i in range(len(result["ids"])):
    list_domain.append(result["metadatas"][i]["area"])
    

list_domain = np.unique(list_domain)
# print(list_domain)
# list_domain_json = {"1" : list(list_domain)}
list_domain_json = json.dumps(list(list_domain))
# print(list_domain_json)
f = open("hackathon-2023/src/list_domaine.json", "w")
f.write(list_domain_json)
f.close()