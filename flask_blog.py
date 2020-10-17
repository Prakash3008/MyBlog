from flask import Flask, escape, request,render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    name = request.args.get("name", "User, this is about page")
    return f'<h1>Hello, {escape(name)}!</h1>'

if __name__ == '__main__':
    app.run(debug=True)