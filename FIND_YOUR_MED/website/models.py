#from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from website.storage.connectdb import Connectsqldb
from sqlalchemy import MetaData, Table, Column, Integer, String, inspect
from sqlalchemy import create_engine, MetaData


class User(Connectsqldb):
    __tablename__ = 'pharm_user'
    id = Column('id', Integer, primary_key=True)
    pharmacy_name = Column('pharmacy_name', String(255))
    phonenumber = Column('phonenumber', String(20))
    address = Column('address', String(255))
    pharmacy_mail = Column('pharmacy_mail', String(255))
    password = Column('password', String(255))

    def __init__(self, pharmacy_name, phonenumber, address, pharmacy_mail, password):
        self.pharmacy_name = pharmacy_name
        self.phonenumber = phonenumber
        self.address = address
        self.pharmacy_mail = pharmacy_mail
        self.password = password
    """__tablename__ = 'pharm_user'
    id = Column('id', Integer, primary_key=True),
    pharmacy_name =Column('pharmacy_name', String(255)),
    phonenumber = Column('phonenumber', String(20)),
    address = Column('address', String(255)),
    pharmacy_mail = Column('pharmacy_mail', String(255))
    password = Column('password', String(255))"""

    """def __init__(self):
        self.metadata = MetaData()
        self.user_table = Table(
            "pharm_user",
            self.metadata,
            Column('id', Integer, primary_key=True),
            Column('pharmacy_name', String(255)),
            Column('phonenumber', String(20)),
            Column('address', String(255)),
            Column('pharmacy_mail', String(255)),
            Column('password', String(255))
        )"""
