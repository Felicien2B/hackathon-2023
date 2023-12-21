from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Une liste d'exemple d'articles
articles = [
    {'id': 1, 'title': 'Article 1', 'content': 'Contenu de l\'article 1', 'keywords': ['python', 'flask']},
    {'id': 2, 'title': 'Article 2', 'content': 'Contenu de l\'article 2', 'keywords': ['web', 'development']},
    {'id': 3, 'title': 'Article 3', 'content': 'Contenu de l\'article 3', 'keywords': ['data', 'science']},
]

# Routes de l'application

# Recherche d'articles
@app.route('/', methods=['GET', 'POST'])
def search():
    matching_articles = []
    if request.method == 'POST':
        search_query = request.form['search']
        # Filtrer les articles correspondant à la recherche
        matching_articles = [article for article in articles if search_query.lower() in article['title'].lower()]
    return render_template('index.html', articles=matching_articles)

# Sélection d'un article
@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        return render_template('article.html', article=article)
    return 'Article non trouvé', 404


if __name__ == '__main__':
    app.run(debug=True)
