from flask import Flask, render_template, request

app = Flask(__name__)

articles = [
    {'id': 3, 'title': 'Article 1', 'content': 'Le modèle vectoriel est relativement simple à appréhender (algèbre linéaire) et est facile à implémenter. Il permet de retrouver assez efficacement des documents dans un corpus non structuré (recherche dinformation), son efficacité dépendant pour une grande part de la qualité de la représentation (vocabulaire et schéma de pondération). La représentation vectorielle permet aussi une mise en correspondance des documents avec une requête imparfaite', 'keywords': ['python', 'flask']},
    {'id': 8, 'title': 'Article 2', 'content': 'Contenu de l\'article 8', 'keywords': ['web', 'development']},
    {'id': 15, 'title': 'Article 3', 'content': 'Contenu de l\'article 15', 'keywords': ['data', 'science']},
]

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

if __name__ == '__main__':
    app.run(debug=True)
