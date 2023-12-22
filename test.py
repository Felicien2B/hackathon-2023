import chromadb
from chromadb.config import Settings
import json
import numpy as np

client = chromadb.PersistentClient(path="hackathon-2023/bdd")
# collection permet de stocker embeddings, documents et autre metadata
collection = client.get_or_create_collection(name="article")

result = collection.get(ids=["232456789"])


# result = collection.get(ids=list_id)

list_domain = []

print(result)
print(len(result["ids"]))

result_list = []
if(len(result["ids"]) != 0):
    for i in range(len(result["ids"])):
            id = result["ids"][i]
            keyword = result["metadatas"][i]["keywords"]
            abstract = result["metadatas"][i]["abstract"]
            result_list.append({
                "id": id,
                "keywords" : keyword,
                "abstract" : abstract
            })
else:
    result_list.append("None")
        
print(json.dumps(result_list))




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