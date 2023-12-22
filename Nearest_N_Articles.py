import numpy as np
from scipy.spatial.distance import cosine
import pandas as pd

def NearestNArticles(idArticle, n):
    """calcule les distances (avec cosine) entre les embeddings de idArticle et ceux des articles de la base
    renvoie les n articles les plus proches

    Args:
        idArticle (int): représente l'id de l'article courant
        n (int): représente le nombre d'articles connexes à renvoyer

    Returns:
        list[int]: list d'entiers représentants les id des n articles connexes
    """
    df = pd.read_excel("hackathon-2023\Hackathon2023_CleanDataEmbedding.xlsx")
    z=idArticle
    
    # traitement pour récupérer les embeddings sous la forme de list de float
    embeddings = df['keywords_embeddings']
    df["new_embeddings"] = df["keywords_embeddings"].apply(lambda x: x.replace("[", "").replace("]", "").replace("\n", "").split())
    df["new_embeddings"] = df["new_embeddings"].apply(lambda x: [float(i) for i in x])
    query_embedding = [float(i) for i in embeddings[z].replace("[", "").replace("]", "").split()]
    
    # calcule des distance entre l'article courant et les autres articles
    df["distances"] = df["new_embeddings"].apply(lambda x: cosine(query_embedding, x))
    
    # on récupère les plus petites distances
    smallest_distances = df.nsmallest(n+1, 'distances')[[ "keywords_embeddings", "distances"]]
    indices_of_smallest_distances = smallest_distances.index.tolist()
    
    # conversion des index en string (pour la requête de la base)
    indices_of_smallest_distances = [str(x) for x in indices_of_smallest_distances]

    return indices_of_smallest_distances[1:]
    
