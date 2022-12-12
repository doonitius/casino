from model.game import GameBoard

user_list = []
game_list = GameBoard()
account_list = []
transaction_list = []

def id_generator(obj_list):
    return len(obj_list) + 1

def getUserList():
    return user_list

def getGameList():
    return game_list

def getAccountList():
    return account_list

def getTransactionLogList():
    return transaction_list

def updateUserList(updated_user_list):
    global user_list 
    user_list = updated_user_list

def updateGameList(updated_game_list):
    global game_list 
    game_list = updated_game_list

def updateAccountList(updated_account_list):
    global account_list  
    account_list  = updated_account_list

def updateTransactionList(update_transaction_list):
    global transaction_list 
    transaction_list = update_transaction_list
