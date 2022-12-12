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

    @abstractmethod
    def isAdmin(self):
        return False

    def __del__(self):
        print("user deleted")

class Admin(User):
    def __init__(self, user_id,user_name, password):
        User.__init__(self, user_id, user_name ,password)

    def addGame(self):
        print('add game')

    def EditGame(self):
        print("edit game")

    def DeleteGame(self):
        print('delete game')

    def AddMoneyPool(self):
        print('add money pool')

    def isAdmin(self):
        return True
    