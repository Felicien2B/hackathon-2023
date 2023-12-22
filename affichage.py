# récupère le résultat d'une requête
# le met au format json et le renvoie
def get_resultat_requete(result):
    result_list = []
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