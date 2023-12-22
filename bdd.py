# crée la base de données et la remplie avec les données de l'excel
# permannante donc pas besoin relancer le script à chaque fois

import chromadb
from chromadb.config import Settings
import pandas as pd

# si jamais il faut la relancer à chaque fois :
# faire une fonction
# client.reset

#dataframe pour récupérer les données à mettre
df = pd.read_excel("hackathon-2023\Hackathon2023_CleanDataEmbedding.xlsx")

client = chromadb.PersistentClient(path="hackathon-2023/bdd")
# chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="hackathon-2023/bdd2/"))
# client.reset()
# collection permet de stocker embeddings, documents et autre metadata
collection = client.get_or_create_collection(name="article")
# print(collection.count())

#normaliser la colonne keywords_embeddings
df["new_keywords_embeddings"] = df["keywords_embeddings"].apply(lambda x : x.replace("[", "").replace("]","").replace("\n", "").split())
df["new_keywords_embeddings"] = df["new_keywords_embeddings"].apply(lambda y : [float(i) for i in y])
df["area"] = df["area"].apply(lambda x : x.strip().lower())

# on ajoute chaque row de la df à la base
for ind in df.index:
    collection.add(embeddings=df["new_keywords_embeddings"][ind], metadatas=[{"area": df["area"][ind], "keywords": df["keywords"][ind],"abstract": df["abstract"][ind]}], ids=str(ind))
    
