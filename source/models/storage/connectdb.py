#!/usr/bin/python3
"""
Shebang to creae a PY script
"""


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
        duser = os.getenv("DATABASE_USER")
        dhost = os.getenv("DATABASE_HOST")
        dpassword = os.getenv("DATABASE_PASSWORD")
        dport = os.getenv("DATABASE_PORT")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(duser, dpassword, dhost, dport, dname))
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def new(self, data):
        """add new data to the DB"""
        try:
            self.__session.add(data)
            self.__session.commit()
        except Exception as e:
            print("Error:", e)
            self.__session.rollback()

    def delete_row(self, med_id):
        """delete a medecine from DB"""
        try:
            self.__session.delete(med_id)
            self.__session.commit()
        except Exception as e:
            print("Error:", e)
            self.__session.rollback()

    def close(self):
        """Close the session"""
        self.__session.close()

    def get_user_by_email(self, email):
        """Query the database for a user by email"""
        from source.models.user import Adduser
        try:
            user = self.__session.query(Adduser).filter_by(pharmacy_mail=email).first()
            return user
        except Exception as e:
            print("Error:", e)
            return None

    def get_data_by_id(self, id):
        """Query the database to retrieve data by id"""
        from source.models.user import Adduser
        try:
            user = self.__session.query(Adduser).filter_by(id=id).first()
            return user
        except Exception as e:
            print("Error:", e)
            return None

    def get_data_by_name(self, name):
        """Query the database for a medecine details by by name"""
        from source.models.medecine import Addmedecine
        try:
            name = self.__session.query(Addmedecine).filter(Addmedecine.med_name.ilike(f"%{name}%")).all()
            return name
        except Exception as e:
            print("Error:", e)
            return None

    def get_data_by_pharm_id(self, id):
        """Query the database for a medecine details by by pharmacy_id"""
        from source.models.medecine import Addmedecine
        try:
            id = self.__session.query(Addmedecine).filter(Addmedecine.pharmacy_id == id).all()

            return id
        except Exception as e:
            print("Error:", e)
            return None

    def get_data_by_med_id(self, id):
        """Query the database for a medecine details by by med_id"""
        from source.models.medecine import Addmedecine
        try:
            id = self.__session.query(Addmedecine).filter_by(id=id).first()

            return id
        except Exception as e:
            print("Error:", e)
            return None
