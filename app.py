
import keyword
from flask import Flask, render_template, request
import chromadb
from chromadb.config import Settings

app = Flask(__name__)

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
    chroma_client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="hackathon-2023/bdd/"))
    # collection permet de stocker embeddings, documents et autre metadata
    collection = chroma_client.get_or_create_collection(name="article") 
    
    # article avec domaine de précisé
    if request.method == 'POST':
        search_query = request.form['search'].lower()
        result = collection.get(where={"area" : search_query})
    elif request.method == "GET":
        result = collection.get()

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

  
# @app.route('/get_domain', methods="GET")
# def get_domain():
       



if __name__ == '__main__':
    app.run(debug=True)
