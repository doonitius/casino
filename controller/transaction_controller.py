from model.account import TransactionLog
from controller.object_controller import getTransactionLogList
from controller.account_controller import findAccount

def showTransactionLog(user_id):
    user_account = findAccount(user_id)
    account_id = user_account.getAccountId()
    transaction_list = getTransactionLogList()

    result = []
    for transaction in transaction_list:
        if account_id == transaction.getAccountId():
            result.append(transaction)

    return result