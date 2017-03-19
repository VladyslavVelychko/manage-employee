from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, DateField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Employee

class RegistrationForm(FlaskForm):
	#Creation of new account

	email=StringField('Email', validators=[DataRequired(), Email()])
	username=StringField('Username',validators=[DataRequired()])
	first_name=StringField('First name',validators=[DataRequired()])
	last_name=StringField('Last name',validators=[DataRequired()])
	birthday=DateField('Birthday',validators=[DataRequired()],description='format:2012-01-01')
	phone=StringField('Phone',validators=[DataRequired()],description='format:+380630000000')
	password=PasswordField('Password',validators=[DataRequired(),EqualTo('confirm_password')])
	confirm_password=PasswordField('Confirm password')
	submit=SubmitField('Register')

	def validate_email(self,field):
		if Employee.query.filter_by(email=field.data).first():
			raise ValidationError('Email is already using')

	def validate_username(self,field):
		if Employee.query.filter_by(username=field.data).first():
			raise ValidationError('Username is already using')

class LoginForm(FlaskForm):
	#Users login

	email=StringField('Email',validators=[DataRequired(),Email()])
	password=PasswordField('Password',validators=[DataRequired()])
	submit=SubmitField('Login')