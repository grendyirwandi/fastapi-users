from pymongo import MongoClient
from app.config.mongo import db

class ConnectionMongo:

    def __init__(self):
        self.__conn = MongoClient(db['url'])

    @property
    def conn(self):
        return self.__conn['qqplays']