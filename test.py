from controller.user_controller import addUserToList, showUserList, addAdminToList
from controller.account_controller import accountDeposit, accountGetBalance, accountWithdraw

addUserToList('jade', '8888')

showUserList()

print(accountGetBalance(1))

accountDeposit(1, 100, 'Deposit')

print(accountGetBalance(1))

accountWithdraw(1, 50, 'Withdraw')

print(accountGetBalance(1))
