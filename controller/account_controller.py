from model.account import TransactionLog
from controller.object_controller import id_generator, getAccountList, updateTransactionList, getTransactionLogList, updateAccountList


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