
import json
from flask import Flask, render_template, request
import chromadb

from Nearest_N_Articles import NearestNArticles
from affichage import get_resultat_requete

app = Flask(__name__)

client = chromadb.PersistentClient(path="bdd")
collection = client.get_or_create_collection(name="article") 
print(collection.count())



# route par défaut
@app.route('/', methods=['GET', 'POST'])
def search():
    matching_articles = []
    # renvoie les article en fonction du domaine spécifié en entrée
    if request.method == 'POST':
        search_query = request.form['search']
        # récupère les articles du domaine
        result = collection.get(where={"area" : search_query})
        # renvoie le résultat sous la forme : [{"id" : , "abstract" ; , "keywords" : }, {}]
        result_list = get_resultat_requete(result)
        print(result)
        print(result_list)
        matching_articles = [
            article for article in result_list
            if any(keyword in search_query for keyword in article['keywords'])
        ]
    # renvoie la liste des domaines
    # les load depuis un fichier
    f = open("src/list_domaine.json", 'r')
    res = json.load(f)
    print(res)
    f.close()
    return render_template('index.html', articles=matching_articles, res=res)

@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        return render_template('article.html', article=article)
    return 'Article non trouvé', 404


# renvoie la liste d'articles en fonciton du domaine spécifié
@app.route('/list_article', methods=['GET', 'POST'])
def get_list_article():
    
    # pour tous les articles du domaine précisé
    if request.method == 'POST':
        search_query = request.form['search'].lower()
        result = collection.get(where={"area" : search_query})
    # pour renvoyer tous les articles
    elif request.method == "GET":
        result = collection.get()

    # renvoie le résultat sous la forme : [{"id" : , "abstract" ; , "keywords" : }, {}]
    result_list = get_resultat_requete(result)
        
    return result_list

# renvoie les id des articles connexes à l'article courant
@app.route('/get_article_connexe', methods=["POST"])
def get_article_connexe():

    # récupère le nombre d'article connexe
    nb_article_connexe = int(request.form["relatedArticles"])
    
    # récupère l'id de l'article courant
    id_article = int(request.form["idArticle"])
    
    # appelle la fonction pour récupérer un tableau des id des articles connexes
    res = NearestNArticles(id_article, nb_article_connexe)
    
    # récupère les infos des articles connexes
    result = collection.get(ids=res)
    
    # renvoie le résultat sous la forme : [{"id" : , "abstract" ; , "keywords" : }, {}]
    result_list = get_resultat_requete(result)
        
    return result_list


# renvoie un article grâce à son id
@app.route('/get_article', methods=["POST"])
def get_article():
    
    # récupère l'id de l'article à afficher
    id_query = request.form['search'].lower()
    # récupère les infos de l'article
    result = collection.get(ids=[id_query])

    # renvoie le résultat sous la forme : [{"id" : , "abstract" ; , "keywords" : }, {}]
    result_list = get_resultat_requete(result)

    
    return result_list
        



if __name__ == '__main__':
    app.run(debug=True)
