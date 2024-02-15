#!/usr/bin/python3
from source.models.storage.connectdb import Connecttodb
def test_connection(self):
        """Test the database connection"""
        try:
            with self.__engine.connect() as connection:
                connection.execute("SELECT 1")
                print("Database connection successful")
        except OperationalError as e:
            print("Database connection error:", e)
