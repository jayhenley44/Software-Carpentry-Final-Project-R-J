from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', year=datetime.now().year)

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', year=datetime.now().year)

@app.route('/blog')
def blog():
    return render_template('blog.html', year=datetime.now().year)

@app.route('/about')
def about():
    return render_template('about.html', year=datetime.now().year)

@app.route('/contact')
def contact():
    return render_template('contact.html', year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)
