#!/usr/bin/python3
"""
SHEBANG to create a PY SCRIPT
"""

import source.models
import uuid
from datetime import datetime
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData, Table, Integer, inspect, ForeignKey
from source.models.storage.connectdb import Connecttodb
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Addmedecine(Connecttodb, Base):
    """class to handle adding users"""
    __tablename__ = 'med_details'
    id = Column('id', String(255), primary_key=True)
    med_name = Column('med_name', String(255))
    med_description = Column('med_description', String(20))
    quantity = Column('quantity', String(255))
    created_at = Column('created_at', default=datetime.now)
    pharmacy_id = Column('pharmacy_id', String(255))

    def __init__(self, med_name, med_description, quantity, pharmacy_id):
        """initialization fo Addmedecine"""
        self.id = str(uuid.uuid4())
        self.med_name = med_name
        self.med_description = med_description
        self.quantity = quantity
        self.pharmacy_id = pharmacy_id

    @staticmethod
    def get_data_by_name(name):
        """Get data by name"""
        try:
            connector = Connecttodb()
            user = connector.get_data_by_name(name)
            return user
        except Exception as e:
            print("Error:", e)
            return None
