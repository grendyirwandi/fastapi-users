from app.config.database import db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class ConnectionDb:
    def __init__(self):
        self.__engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s' %
                               (db['username'], db['password'], db['hostname'], db['port'], db['database']))
        self.__conn = self.__engine.connect()
        try:
            print('Your connection ok \n connection object is: {}'.format(self.__conn))
        except:
            print('Your connection not connected')

    @property
    def conn(self):
        return self.__engine

    @property
    def session(self):
        Session = sessionmaker(bind=self.__engine)
        return Session()

    @property
    def Base(self):
        return declarative_base()