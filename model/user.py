class User:
    def __init__(self, user_id, password):
        self.__user_id = user_id
        self.__password = password

    def getUserId(self):
        return self.__user_id

    def getPassword(self):
        return self.__password

    def setUserId(self, user_id):
        self.__user_id = user_id

    def setPassword(self, password):
        self.__password = password

class Admin(User):
    def __init__(self, user_id, password):
        super().__init__(self, user_id, password)

    def addGame(self):
        pass

    def EditGame(self):
        pass

    def DeleteGame(self):
        pass

    def AddMoneyPool(self):
        pass
    