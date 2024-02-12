#!/usr/bin/python3

import os
import uuid
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, inspect
from sqlalchemy.orm import scoped_session, sessionmaker



env_file_path = "/home/jirafasha/Desktop/MED_FINDER/website"
load_dotenv(dotenv_path=os.path.join(env_file_path, ".env"))
dname = os.getenv("DATABASE_NAME")
duser=os.getenv("DATABASE_USER") 
dhost=os.getenv("DATABASE_HOST") 
dpassword=os.getenv("DATABASE_PASSWORD") 
dport=os.getenv("DATABASE_PORT")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}:{}/{}'.format(duser, dpassword, dhost,dport, dname)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Adduser(db.Model):
	__tablename__ = 'pharm_user'
	id = Column('id', String(255), primary_key=True)
	pharmacy_name = Column('pharmacy_name', String(255))
	phonenumber = Column('phonenumber', String(20))
	address = Column('address', String(255))
	pharmacy_mail = Column('pharmacy_mail', String(255))
	password = Column('password', String(255))
	created_at = Column('created_at',default=datetime.now) 

	def __init__(self, pharmacy_name, phonenumber, address, pharmacy_mail, password):
		self.id = str(uuid.uuid4())
		self.pharmacy_name = pharmacy_name
		self.phonenumber = phonenumber
		self.address = address
		self.pharmacy_mail = pharmacy_mail
		self.password = password

	def new(data):
		try:
			with app.app_context():
				db.session.add(data)
				db.session.commit()
		except :
			print("duplicate")
