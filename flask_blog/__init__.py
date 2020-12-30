from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor

app = Flask(__name__)
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)

app.config['SECRET_KEY'] = '97cbe610e659841c81815c7a2c5e339adfc316f7bd1028ab9a0fd40ae63071cb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flask_blog import routes