# from app.core.ConnectionRedis import ConnectionRedis
from app.core.ConnectionDb import ConnectionDb
import json
import pandas as pd
from datetime import datetime
import uuid

class Users_model:
    def __init__(self):
        # self.__redis = ConnectionRedis().conn
        self.__db = ConnectionDb().conn
        self.__session = ConnectionDb().session
    
    def getAllUsers(self):
        try:
            data = []
            df = pd.read_sql('SELECT id, name, address, createdAt, updatedAt FROM users ', con=self.__db)
            data = df.to_dict(orient='records')
            return data
        except:
            return {"status": 500, "message": "Internal server error"}

    def getSpesificUsers(self, id):
        try:
            df = pd.read_sql("SELECT id, name, address, createdAt, updatedAt FROM users WHERE `id`= '{}' LIMIT 1;".format(id), con=self.__db)
            data = df.to_dict(orient='records')
            return data[0]
        except:
            return False

    def addUsers(self, data):
        Session = self.__session
        try:
            Session.execute("INSERT INTO `users` (`id`,`name`,`address`,`createdAt`) VALUES ('{}','{}','{}','{}');".format(str(uuid.uuid4()), data.name, data.address, datetime.now()))
            Session.commit()
            return {"status": 200, "message": "Success!"}
        except ZeroDivisionError:
            print(traceback.format_exc())
            print('masuk catch')
            print("Error : ", ex)
            Session.rollback()
            return {"status": 500, "message": "Internal server error"}
        finally:
            Session.close()
            
    def updateUsers(self, id, data):
        Session = self.__session
        try:
            Session.execute("UPDATE `users` SET `name`='{}' ,`address`='{}', `updatedAt`='{}' WHERE `id`= '{}';".format(data.name, data.address, datetime.now(), id))
            Session.commit()
            return {"status": 200, "message": "Success!"}
        except ZeroDivisionError:
            print(traceback.format_exc())
            print('masuk catch')
            print("Error : ", ex)
            Session.rollback()
            return {"status": 500, "message": "Internal server error"}
        finally:
            Session.close()
            
    def deleteUsers(self, id):
        Session = self.__session
        try:
            Session.execute("DELETE FROM `users` WHERE `id`= '{}';".format(id))
            Session.commit()
            return {"status": 200, "message": "Success!"}
        except ZeroDivisionError:
            print(traceback.format_exc())
            print('masuk catch')
            print("Error : ", ex)
            Session.rollback()
            return {"status": 500, "message": "Internal server error"}
        finally:
            Session.close()