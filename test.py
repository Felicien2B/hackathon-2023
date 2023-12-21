import chromadb
from chromadb.config import Settings
import json
import numpy as np

chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="hackathon-2023/bdd/"))
# collection permet de stocker embeddings, documents et autre metadata
collection = chroma_client.get_or_create_collection(name="article")

# result = collection.get(ids=["0"])

list_id = [1596, 3422, 4805, 1841, 4200]
list_id = [str(x) for x in list_id]

result = collection.get(ids=list_id)

list_domain = []

print(result["ids"])




# for i in range(len(result["ids"])):
#     list_domain.append(result["metadatas"][i]["area"])
    

# list_domain = np.unique(list_domain)
# # print(list_domain)
# list_domain_json = json.dumps(list(list_domain))
# f = open("hackathon-2023/src/list_domaine.json", "w")
# f.write(list_domain_json)
# f.close()

# print(result["metadatas"][0])
# print(result.keys()) #432