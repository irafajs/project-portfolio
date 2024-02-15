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


class Connecttodb:
    """connect to the db using env variables"""
    __engine = None
    __session = None
    
    def __init__(self):
        """load env variables"""
        env_file_path = "/home/jirafasha/Desktop/MED_FINDER/website"
        load_dotenv(dotenv_path=os.path.join(env_file_path, ".env"))
        dname = os.getenv("DATABASE_NAME")
        duser=os.getenv("DATABASE_USER") 
        dhost=os.getenv("DATABASE_HOST") 
        dpassword=os.getenv("DATABASE_PASSWORD") 
        dport=os.getenv("DATABASE_PORT")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(duser, dpassword, dhost,dport, dname))
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
    """def new(data):
        try:
            with app.app_context():
                db.session.add(data)
                db.session.commit()
        except :
            print("duplicate data")"""

    def new(self, data):
        try:
            self.__session.add(data)
            self.__session.commit()
        except Exception as e:
            print("Error:", e)
            self.__session.rollback()

    def get_user_by_email(self, email):
        """Query the database for a user by email"""
        from source.models.user import Adduser
        try:
            user = self.__session.query(Adduser).filter_by(pharmacy_mail=email).first()
            return user
        except Exception as e:
            print("Error:", e)
            return None
