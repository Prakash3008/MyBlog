from flask import Flask, escape, request,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '97cbe610e659841c81815c7a2c5e339adfc316f7bd1028ab9a0fd40ae63071cb'

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

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data} successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'prak30ash@gmail.com' and form.password.data == '123':
            flash(f'You have successfully logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Unsuccessful login. Enter valid credentials', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)