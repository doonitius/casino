import os
from view.message_box import login_error, login_success

path = os.path.realpath(__file__)

dir = os.path.dirname(path)

dir = dir.replace('controller','data')

os.chdir(dir)

def validateUser(username, password):
    isValid = login(username, password)
    if isValid:
        login_success()
    else:
        login_error()

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
            break
    f.close()
    return access_grant
