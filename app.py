from flask import Flask, render_template, request

app = Flask(__name__)

articles = [
    {'id': 3, 'domain': 'Python', 'abstract': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'keywords': ['python', 'flask']},
    {'id': 8, 'domain': 'Web', 'abstract': 'Contenu de l\'article 2', 'keywords': ['web', 'development']},
    {'id': 15, 'domain': 'Data Science', 'abstract': 'Contenu de l\'article 3', 'keywords': ['data', 'science']},
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
