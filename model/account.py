import datetime
class Account:
    def __init__(self, account_id, user_id):
        self.__account_id = account_id
        self.__user_id = user_id
        self.__balance = 0.0
        # self.__transaction_log = []
        # self.__payment = []

    def getBalance(self):
        return self.__balance

    def getAccountId(self):
        return self.__account_id

    def getUserId(self):
        return self.__user_id

    def deposit(self, amount):
        self.__balance += amount
        # self.__transaction_log.append(TransactionLog(transaction_id, float(amount), payment_type))

    def withdraw(self, amount):
        self.__balance -= amount
        # self.__transaction_log.append(TransactionLog(transaction_id, float(-amount), payment_type))

    # def getTransactionLog(self):
    #     return self.__transaction_log

class TransactionLog:
    def __init__(self, account_id, transaction_id, amount, transaction_type):
        self.__transaction_id = transaction_id
        self.__account_id = account_id
        self.__amount = float(amount)
        self.__transaction_type = transaction_type
        self.__date = datetime.datetime.now()

    def displayTransaction(self):
        return self.__transaction_id, self.__amount, self.__account_id, self.__transaction_type, self.__date

class Payment:
    def __init__(self, payment_id, account_id):
        self.__payment_id = payment_id
        self.__account_id = account_id

class CreditCard(Payment):
    def __init__(self, payment_id, account_id, card_id):
        Payment.__init__(self, payment_id, account_id)
        self.__card_id = card_id

    def getCardId(self):
        return self.__card_id

class Bank(Payment):
    def __init__(self, payment_id, account_id, bank_id):
        Payment.__init__(self, payment_id, account_id)
        self.__bank_id = bank_id

    def getCardId(self):
        return self.__bank_id
