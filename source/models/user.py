#!/usr/bin/python3
"""
SHEBANG to create a py script
"""

import source.models
import uuid
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData, Table, Column, Integer, String, inspect
from source.models.storage.connectdb import Connecttodb
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Adduser(Connecttodb, Base):
    """class to handle adding users"""
    __tablename__ = 'pharm_user'
    id = Column('id', String(255), primary_key=True)
    pharmacy_name = Column('pharmacy_name', String(255))
    phonenumber = Column('phonenumber', String(20))
    address = Column('address', String(255))
    pharmacy_mail = Column('pharmacy_mail', String(255))
    password = Column('password', String(255))
    created_at = Column('created_at', default=datetime.now)

    def __init__(self, pharmacy_name, phonenumber, address, pharmacy_mail, password):
        self.id = str(uuid.uuid4())
        self.pharmacy_name = pharmacy_name
        self.phonenumber = phonenumber
        self.address = address
        self.pharmacy_mail = pharmacy_mail
        self.password = password

    @staticmethod
    def get_user_by_email(email):
        """Get user by email"""
        try:
            connector = Connecttodb()
            user = connector.get_user_by_email(email)
            return user
        except Exception as e:
            print("Error:", e)
            return None

    @staticmethod
    def get_data_by_id(id):
        """Get user by id"""
        try:
            connector = Connecttodb()
            data = connector.get_data_by_id(id)
            return data
        except Exception as e:
            print("Error:", e)
            return None
