from model.account import Account
from model.game import Game
from abc import ABC, abstractmethod
class User:
    def __init__(self, user_id, user_name, password):
        self.__user_id = int(user_id)
        self.__user_name = user_name
        self.__password = password

    def getUserId(self):
        return self.__user_id

    def getUserName(self):
        return self.__user_name

    def getPassword(self):
        return self.__password

    def setUserId(self, user_id):
        self.__user_id = user_id

    def setPassword(self, password):
        self.__password = password

    def __del__(self):
        print("user deleted")
    