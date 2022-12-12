from model.account import Account, TransactionLog
from controller.object_controller import getUserList, updateUserList, id_generator, getAccountList, updateTransactionList, getTransactionLogList, updateAccountList

# def accountGetBalance(user_id):
#     user_list = getUserList()
#     current_user = user_list[user_id-1]

#     print(current_user.getUserName(), "current balance: ", current_user.getUserAccount().getBalance())
#     transaction_log_list = current_user.getUserAccount().getTransactionLog()
#     for i in transaction_log_list:
#         print(i.displayTransaction())

def findAccount(user_id):
    account_list = getAccountList()
    for account in account_list:
        if user_id == account.getUserId():
            return account

def updateAccount(account_id, account):
    account_list = getAccountList()
    account_list[account_id-1] = account
    updateAccountList(account_list)


def accountGetBalance(user_id):
    try:
        current_account = findAccount(user_id)
        return current_account.getBalance()
    except:
        return None


def accountDeposit(user_id, amount, transaction_type):
    try: 
        current_account = findAccount(user_id)
        transaction_log_list = getTransactionLogList()
        transaction_id = id_generator(transaction_log_list)

        account_id = current_account.getAccountId()

        current_account.deposit(amount)
        new_transaction = TransactionLog(current_account.getAccountId(), transaction_id, amount, transaction_type)

        transaction_log_list.append(new_transaction)
        updateAccount(account_id, current_account)
        updateTransactionList(transaction_log_list)

    except:
        print("Error")


def accountWithdraw(user_id, amount, transaction_type):
    try: 
        current_account = findAccount(user_id)
        transaction_log_list = getTransactionLogList()
        transaction_id = id_generator(transaction_log_list)

        account_id = current_account.getAccountId()

        current_account.withdraw(amount)
        new_transaction = TransactionLog(current_account.getAccountId(), transaction_id, -amount, transaction_type)

        transaction_log_list.append(new_transaction)
        updateAccount(account_id, current_account)
        updateTransactionList(transaction_log_list)

    except:
        print("Error")

def checkBalance(amount, current_user):
    balance = accountGetBalance(current_user)
    result = True
    if (balance < float(amount)):
        result = False
    return result

# def accountDeposit(user_id, amount, payment_type):
#     user_list = getUserList()
#     current_user = user_list[user_id-1]

#     user_account = current_user.getUserAccount()

#     transaction_log_list = user_account.getTransactionLog()
#     transaction_id = id_generator(transaction_log_list)

#     user_account.deposit(amount, transaction_id, payment_type)

#     current_user.updateAccount(user_account)

#     user_list[user_id-1] = current_user

#     updateUserList(user_list)


# def accountWithdraw(user_id, amount, payment_type):
#     user_list = getUserList()
#     current_user = user_list[user_id-1]

#     user_account = current_user.getUserAccount()

#     transaction_log_list = user_account.getTransactionLog()
#     transaction_id = id_generator(transaction_log_list)

#     user_account.deposit(amount, transaction_id, payment_type)

#     current_user.updateAccount(user_account)

#     user_list[user_id-1] = current_user

#     updateUserList(user_list)