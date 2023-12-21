from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Une liste d'exemple d'articles
articles = [
    {'id': 3, 'domain': 'Python', 'abstract': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nam aliquam sem et tortor. Ac odio tempor orci dapibus. Nibh cras pulvinar mattis nunc sed blandit libero. Arcu dui vivamus arcu felis bibendum. Vulputate eu scelerisque felis imperdiet proin fermentum leo. Ac auctor augue mauris augue neque gravida in fermentum. Dictum sit amet justo donec enim diam vulputate.', 'keywords': ['python', 'flask']},
    {'id': 8, 'domain': 'Web', 'abstract': 'Contenu de l\'article 8', 'keywords': ['web', 'development']},
    {'id': 15, 'domain': 'Data Science', 'abstract': 'Contenu de l\'article 15', 'keywords': ['data', 'science']},
]

# Routes de l'application

# Recherche d'articles
@app.route('/', methods=['GET', 'POST'])
def search():
    domains = list(set(article['domain'] for article in articles))
    if request.method == 'POST':
        selected_domain = request.form['domain']
        matching_articles = [article for article in articles if article['domain'] == selected_domain]
        return render_template('index.html', articles=matching_articles, domains=domains, selected_domain=selected_domain)
    return render_template('index.html', domains=domains)

# Sélection d'un article
@app.route('/article/<int:article_id>')
def article(article_id):
    article = next((a for a in articles if a['id'] == article_id), None)
    if article:
        return render_template('article.html', article=article)
    return 'Article non trouvé', 404


if __name__ == '__main__':
    app.run(debug=True)
