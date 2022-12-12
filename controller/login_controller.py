import os
from view.message_box import loginError
from view.role_window import selectRole
from controller.user_controller import addUserToList, showUserList

path = os.path.realpath(__file__)

dir = os.path.dirname(path)

dir = dir.replace('controller','data')

os.chdir(dir)

def validateUser(username, password, app):
    isValid, user_role = login(username, password)
    print(user_role)
    if isValid:
        current_user = addUserToList(username, password, user_role)
        showUserList()
        selectRole(app,current_user)
    else:
        loginError()

def isUserNameValid(input_user, username):
    if input_user == username:
        return True


def isPassWordValid(input_password, password):
    if input_password == password:
        return True

def login(username, password):
    validUserName = False
    validPassword = False
    access_grant = False
    f = open("user.txt", "r")
    for line in f:
        user_info = line.split()
        if isUserNameValid(username, user_info[0]):
            validUserName = True

        if isPassWordValid(password, user_info[1]):
            validPassword = True

        if validUserName and validPassword:
            access_grant = True
            role = user_info[2]
            break
    f.close()
    return access_grant, int(role)
