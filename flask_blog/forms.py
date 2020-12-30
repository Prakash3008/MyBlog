from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User
from flask_login import current_user
from flask_ckeditor import CKEditorField

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=3, max=20)])
    
    email = StringField('Email', 
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
        validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken')

    def validate_email(self, email):
        mail = User.query.filter_by(email=email.data).first()
        if mail:
            raise ValidationError('Email ID already exists')

class LoginForm(FlaskForm):
    
    email = StringField('Email', 
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators=[DataRequired()])

    remember = BooleanField('Remember me')

    submit = SubmitField('Login')


class UpdateForm(FlaskForm):
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=3, max=20)])
    
    email = StringField('Email', 
        validators=[DataRequired(), Email()])
    
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username is already taken')

    def validate_email(self, email):
        if email.data != current_user.email:
            mail = User.query.filter_by(email=email.data).first()
            if mail:
                raise ValidationError('Email ID already exists')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')