import chromadb
from chromadb.config import Settings
import json
import numpy as np

def generer_liste_domaines():
    """permet de générer la liste des domaines récupérés grâce à la bdd
    la liste est stockée dans un fichier pour être récupérée depuis le front
    """

    # récupère la base de données
    client = chromadb.PersistentClient(path="hackathon-2023/bdd")
    collection = client.get_or_create_collection(name="article")

    # on récupère tous les articles
    result = collection.get()

    list_domain = []

    # on ajoute chaque domaine à la liste
    for i in range(len(result["ids"])):
        list_domain.append(result["metadatas"][i]["area"])
        
    # on garde seulement les valeurs unique
    list_domain = np.unique(list_domain)
  
    # transformation en json + écriture dans le fichier
    list_domain_json = json.dumps(list(list_domain))
    f = open("hackathon-2023/src/list_domaine.json", "w")
    f.write(list_domain_json)
    f.close()