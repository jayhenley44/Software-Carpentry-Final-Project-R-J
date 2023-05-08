from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from blog_database import init_db, add_post, get_posts

app = Flask(__name__)
init_db()

@app.route('/')
def home():
    return render_template('index.html', year=datetime.now().year)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', year=datetime.now().year)


@app.route('/blog')
def blog():
    posts = get_posts()
    return render_template('blog.html', year=datetime.now().year, posts=posts)

@app.route('/blog/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        published_date = request.form['published_date']

        add_post(title, content, author, published_date)

        return redirect(url_for('blog'))

    return render_template('createpost.html')
@app.route('/about')
def about():
    return render_template('about.html', year=datetime.now().year)

@app.route('/contact')
def contact():
    return render_template('contact.html', year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)
