# affiche le résultat d'une requête sous la forme [{"id" : , "abstract" ; , "keywords" : }, {}]
# si rien n'a été trouvé : []
def get_resultat_requete(result):
    result_list = []
    
    # pour chaque document détecté : on récupère son id, son abstract et ses keyword
    for i in range(len(result["ids"])):
        id = result["ids"][i]
        keyword = result["metadatas"][i]["keywords"]
        abstract = result["metadatas"][i]["abstract"]
        result_list.append({
            "id": id,
            "keywords" : keyword,
            "abstract" : abstract
        })
        
    return result_list