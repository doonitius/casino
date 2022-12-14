from model.user import User
from model.account import Account
from controller.object_controller import id_generator, getUserList, updateUserList, getAccountList, updateAccountList

def addUserToList(user_name, password):

    user_list = getUserList()
    user_id = id_generator(user_list)

    account_list = getAccountList()
    account_id = id_generator(account_list)

    new_user = User(user_id, user_name, password)

    new_account = Account(account_id, user_id)

    account_list.append(new_account)
    user_list.append(new_user)
    
    updateAccountList(account_list)
    updateUserList(user_list)

    return user_id

def showUserList():
    user_list = getUserList()
    for i in user_list:
        print(i.getUserId(), i.getUserName())

def removeUserFromList(user_id):
    user_list = getUserList()
    current_user = user_list.pop(user_id-1)
    del current_user
    updateUserList(user_list)
    print("remain user: ", showUserList())