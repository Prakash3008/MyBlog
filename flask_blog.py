from flask import Flask, escape, request,render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Prakash',
        'title': 'Post 1',
        'content': 'First Post',
        'date_posted': 'April 10, 2020'
    },
    {
        'author': 'Ash',
        'title': 'Post 2',
        'content': 'Second Post',
        'date_posted': 'April 29, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About title')

if __name__ == '__main__':
    app.run(debug=True)