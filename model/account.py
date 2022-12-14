import datetime
class Account:
    def __init__(self, account_id, user_id):
        self.__account_id = account_id
        self.__user_id = user_id
        self.__balance = 0.0

    def getBalance(self):
        return self.__balance

    def getAccountId(self):
        return self.__account_id

    def getUserId(self):
        return self.__user_id

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

class TransactionLog:
    def __init__(self, account_id, transaction_id, amount, transaction_type):
        self.__transaction_id = transaction_id
        self.__account_id = account_id
        self.__amount = float(amount)
        self.__transaction_type = transaction_type
        self.__date = datetime.datetime.now()

    def displayTransaction(self):
        return self.__transaction_id, self.__amount, self.__account_id, self.__transaction_type, self.__date

    def getAccountId(self):
        return self.__account_id
