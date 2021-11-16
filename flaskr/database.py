import mysql.connector as connection
import pandas as pd
from dotenv import dotenv_values
import os

config = dotenv_values(".env")

class Database():
    def __init__(self) -> None:
        self.database = config['DB_NAME']
        self.server = config['DB_SERVER']
        self.user = config['DB_USERID']
        self.password = config['DB_PASSWORD']
        self.port = config['DB_PORT']
    #    self.database = os.environ.get('DB_NAME')
    #    self.server = os.environ.get('DB_SERVER')
    #    self.user = os.environ.get('DB_USERID')
    #    self.password = os.environ.get('DB_PASSWORD')
    #    self.port = os.environ.get('DB_PORT')
    #    self.conn = []
        pass

    def open_connection(self):
        self.conn = connection.connect(host = self.server, database = self.database, user = self.user,
            password = self.password, port = self.port)
        pass

    def close_connection(self):
        self.conn.close()
        pass

# En teoria esto es para facilitar la obtencion y manipulacion de datos, no se me ocurrre un mejor nombre por ahora
    def query_data(self, query = ""):    
        self.open_connection()
        dataframe = pd.read_sql(query, self.conn)
        self.close_connection()
        return dataframe

    pass