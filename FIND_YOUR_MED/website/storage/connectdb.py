#!/usr/bin/python3

import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from sqlalchemy.exc import ProgrammingError
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String, inspect
from sqlalchemy.orm import scoped_session, sessionmaker



class Connectsqldb():

  __engine = None
  __session = None
  
  def __init__(self):
    env_file_path = "/home/jirafasha/Desktop/MED_FINDER/website"
    load_dotenv(dotenv_path=os.path.join(env_file_path, ".env"))
    dname = os.getenv("DATABASE_NAME")
    duser=os.getenv("DATABASE_USER") 
    dhost=os.getenv("DATABASE_HOST") 
    dpassword=os.getenv("DATABASE_PASSWORD") 
    dport=os.getenv("DATABASE_PORT")

    db = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(duser, dpassword, dhost,dport, dname))
    connection = db.connect()
    print("conntected to the db")

    def new(self, data):
      new_user = User(**data)
      self.__session.add(new_user)
      self.save()

    def save(self):
      self.__session.commit()

