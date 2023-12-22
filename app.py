
import json
from flask import Flask, render_template, request
import chromadb

from Nearest_N_Articles import NearestNArticles
from affichage import get_resultat_requete

app = Flask(__name__)

client = chromadb.PersistentClient(path="hackathon-2023/bdd")
collection = client.get_or_create_collection(name="article") 


# articles = [
#     {'id': 3, 'domain': 'Python', 'abstract': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'keywords': ['python', 'flask']},
#     {'id': 8, 'domain': 'Web', 'abstract': 'Contenu de l\'article 2', 'keywords': ['web', 'development']},
#     {'id': 15, 'domain': 'Data Science', 'abstract': 'Contenu de l\'article 3', 'keywords': ['data', 'science']},
# ]

@app.route('/', methods=['GET', 'POST'])
def search():
    matching_articles = []
    if request.method == 'POST':
        search_query = request.form['search'].lower()
        matching_articles = [
            article for article in articles
            if any(keyword in search_query for keyword in article['keywords'])
        ]
    return render_template('index.html', articles=matching_articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        return render_template('article.html', article=article)
    return 'Article non trouvé', 404


# renvoie la liste d'articles
@app.route('/list_article', methods=['GET', 'POST'])
def get_list_article():
    # chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="hackathon-2023/bdd/"))
    # # collection permet de stocker embeddings, documents et autre metadata
    # collection = chroma_client.get_or_create_collection(name="article") 
    
    # pour tous les articles du domaine précisé
    if request.method == 'POST':
        search_query = request.form['search'].lower()
        result = collection.get(where={"area" : search_query})
    # pour renvoyer tous les articles
    elif request.method == "GET":
        result = collection.get()

    # renvoie le résultat
    result_list = get_resultat_requete(result)
    # for i in range(len(result["ids"])):
    #     id = result["ids"][i]
    #     keyword = result["metadatas"][i]["keywords"]
    #     abstract = result["metadatas"][i]["abstract"]
    #     result_list.append({
    #         "id": id,
    #         "keywords" : keyword,
    #         "abstract" : abstract
    #     })
        
    return result_list

# renvoie la liste des domaines
# les load depuis un fichier
@app.route('/get_domain', methods=["GET"])
def get_domain():
    f = open("hackathon-2023/src/list_domaine.json")
    res = json.load(f)
    f.close()
    return res

# a vérifier (une fois qu'on a récupérer l'id de l'article depuis le front)
# plus faire proprement
@app.route('/get_article_connexe', methods=["GET", "POST"])
def get_article_connexe():
    # chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="hackathon-2023/bdd/"))
    # # collection permet de stocker embeddings, documents et autre metadata
    # collection = chroma_client.get_or_create_collection(name="article")
    nb_article_connexe = request.form["relatedArticles"]
    
    
    id_article = 1
    
    
    res = NearestNArticles(id_article, nb_article_connexe)
    
    res = [str(x) for x in res]
    result = collection.get(ids=res)
    
    result_list = get_resultat_requete(result)
    
    # for i in range(len(result["ids"])):
    #     id = result["ids"][i]
    #     keyword = result["metadatas"][i]["keywords"]
    #     abstract = result["metadatas"][i]["abstract"]
    #     result_list.append({
    #         "id": id,
    #         "keywords" : keyword,
    #         "abstract" : abstract
    #     })
        
        
    return result_list


# a vérifier + faire proprement
@app.route('/get_article', methods=["GET", "POST"])
def get_article():
    # chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="hackathon-2023/bdd/"))
    # # collection permet de stocker embeddings, documents et autre metadata
    # collection = chroma_client.get_or_create_collection(name="article") 
    
    
    if request.method == 'POST':
        id_query = request.form['search'].lower()
        result = collection.get(ids=[id_query])


    result_list = get_resultat_requete(result)
    # id = result["ids"]
    # keyword = result["metadatas"][0]["keywords"]
    # abstract = result["metadatas"][0]["abstract"]
    # result_list.append({
    #     "id": id,
    #     "keywords" : keyword,
    #     "abstract" : abstract
    # })
    
    return result_list
        

    

    
    
    
    
    
       



if __name__ == '__main__':
    app.run(debug=True)
