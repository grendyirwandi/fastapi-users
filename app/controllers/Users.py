from app.core.Controller import Controller
import threading
from datetime import datetime
import math
import pandas as pd
import numpy as np

class Users(Controller):
    
    def __init__(self):
        self.__usersModel = self.model('Users_model')

    def getAllUsers(self):
        return self.__usersModel.getAllUsers()

    def getSpesificUsers(self, id):
        return self.__usersModel.getSpesificUsers(id)

    def addUsers(self, data):
        return self.__usersModel.addUsers(data)
        
    def updateUsers(self, id, data):
        return self.__usersModel.updateUsers(id, data)

    def deleteUsers(self, id):
        return self.__usersModel.deleteUsers(id)