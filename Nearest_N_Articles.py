import numpy as np
from scipy.spatial.distance import cosine
import pandas as pd

def NearestNArticles(idArticle, n):
    df = pd.read_excel("hackathon-2023\Hackathon2023_CleanDataEmbedding.xlsx")
    z=idArticle
    embeddings = df['keywords_embeddings']
    df["new_embeddings"] = df["keywords_embeddings"].apply(lambda x: x.replace("[", "").replace("]", "").replace("\n", "").split())
    df["new_embeddings"] = df["new_embeddings"].apply(lambda x: [float(i) for i in x])
    query_embedding = [float(i) for i in embeddings[z].replace("[", "").replace("]", "").split()]
    
    df["distances"] = df["new_embeddings"].apply(lambda x: cosine(query_embedding, x))
    smallest_distances = df.nsmallest(n+1, 'distances')[[ "keywords_embeddings", "distances"]]
    indices_of_smallest_distances = smallest_distances.index.tolist()
    
    indices_of_smallest_distances = [str(x) for x in indices_of_smallest_distances]

  
    # return smallest_distances, indices_of_smallest_distances[1:]
    return indices_of_smallest_distances[1:]
    
# res = NearestNArticles(1, 5)
# print(res)