from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Employee(UserMixin, db.Model):
	#Creating an Employee table

	__tablename__='employees'

	id=db.Column(db.Integer, primary_key=True)
	email=db.Column(db.String(60),index=True, unique=True)
	username=db.Column(db.String(60), index=True,unique=True)
	first_name=db.Column(db.String(60),index=True)
	last_name=db.Column(db.String(60),index=True)
	birthday=db.Column(db.DateTime,index=True)
	phone=db.Column(db.String(13),index=True,default='+380630000000')
	password_hash=db.Column(db.String(128))
	department_id=db.Column(db.Integer,db.ForeignKey('departments.id'))
	role_id=db.Column(db.Integer,db.ForeignKey('roles.id'))
	is_admin=db.Column(db.Boolean,default=False)

	@property
	def password(self):
	#Prevention for password being accessed
		raise AttributeError('password is not a readable attribute.')

	@password.setter
	def password(self,password):
	#set pass to a hashing pass
		self.password_hash=generate_password_hash(password)

	def verify_password(self,password):
	#check hash pass matches actual pass
		return check_password_hash(self.password_hash,password)

	def __repr__(self):
		return '<Employee: {}>'.format(self.username)

#setting up user_loader
@login_manager.user_loader
def load_user(user_id):
	return Employee.query.get(int(user_id))

class Department(db.Model):
	#Dept table

	__tablename__='departments'

	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(60),unique=True)
	description=db.Column(db.String(200))
	employees=db.relationship('Employee',backref='department',lazy='dynamic')

	def __repr__(self):
		return '<Deparment: {}>'.format(self.name)

class Role(db.Model):
	#Role table

	__tablename__='roles'

	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(60),unique=True)
	description=db.Column(db.String(200))
	employees=db.relationship('Employee',backref='role',lazy='dynamic')

	def __repr__(self):
		return '<Role: {}>'.format(self.name)