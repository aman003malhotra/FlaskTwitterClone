from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileAllowed,FileField
from flask_uploads import IMAGES

class RegisterForm(FlaskForm):
	name = StringField('Full name', validators=[InputRequired('A full name is required'), Length(max=100, message='You name can\'t be more than 100 characters')])
	username = StringField('username', validators=[InputRequired('Username is required'), Length(max=30, message='Your username is too many characters')])
	password = PasswordField('Password', validators=[InputRequired('A Password is required')])
	image = FileField(validators=[FileAllowed(IMAGES, 'Only images are accepted')])

class LoginForm(FlaskForm):
	username = StringField('Username',validators=[InputRequired('Username is required'), Length(max=30, message='Your username is too many characters')])
	password = StringField('Password',validators=[InputRequired('A Password is required')])
	remember = BooleanField('Remeber me')

class TweetForm(FlaskForm):
	text = TextAreaField('Message', validators=[InputRequired('Message is Required')])