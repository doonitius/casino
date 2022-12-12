from tkinter import *
from tkinter import ttk
from controller.user_controller import removeUserFromList
from controller.account_controller import accountGetBalance, accountDeposit, accountWithdraw
from controller.transaction_controller import showTransactionLog
import view.game_window
import view.message_box 


# call from many file should move it to another file
def closeWindow(app):
    app.destroy()

def userLogOut(app, current_user):
    removeUserFromList(current_user)
    app.destroy()

# No ref
# def getBalance(current_user):
#     print("current balance",accountGetBalance(current_user))

# Maybe should move to another file
def validateMoney(value, action, current_user):
    check = view.game_window.checkInt(value)
    if (not check):
        view.message_box.inputError()
    else: 
        # make this another function then call it
        balance = accountGetBalance(current_user)
        match action:
            case 1:
                accountDeposit(current_user, float(value), 'Deposit money')
                view.message_box.depositMes(balance, value)
            case 2:
                if (balance < float(value)):
                    view.message_box.lowAmountError(balance, value)
                else:
                    accountWithdraw(current_user, float(value), 'Withdraw money')
                    view.message_box.withdrawMes(balance, value)

    
# Remove admin
# def selectRole(last_window, current_user):
#     closeWindow(last_window)
#     app = Tk()
#     app.title("Select role @Menu")

#     user_button = Button(app, text='User',
#                         command=lambda: userMenuWindow(app, current_user))
#     admin_button = Button(app, text='Admin',
#                         command=lambda: adminMenuWindow(app, current_user))
#     logout_button = Button(app, text='Logout',
#                         command=lambda: userLogOut(app, current_user))
    
#     user_button.grid(row=0,column=0)
#     admin_button.grid(row=0,column=1)
#     logout_button.grid(row=0,column=2)

#     app.geometry("400x200")
#     app.mainloop()

def viewTransaction(current_user):
    app = Tk()
    app.title("Transaction")

    transaction_list = showTransactionLog(current_user)
    i = 0
    for transaction in transaction_list:
        print(transaction.displayTransaction())
        label = Label(app, text=transaction.displayTransaction())
        label.grid(row=i, column=1)
        i += 1
    app.geometry("300x300")
    app.mainloop()



def userMenuWindow(last_window, current_user):
    closeWindow(last_window)

    app = Tk()
    app.title("User menu @Menu")
    tabControl = ttk.Notebook(app)

    tab_play = ttk.Frame(tabControl)
    tab_pay = ttk.Frame(tabControl)

    tabControl.add(tab_play, text='Play')
    tabControl.add(tab_pay, text='Pay')
    tabControl.pack(expand=1, fill="both")

    ttk.Label(tab_play, text='Let play game in Jade Noi 888').grid(column=0,row=0)
    Button(tab_play, text='RPS',command=lambda: view.game_window.rpsMainWindow(app,current_user)).grid(column=0,row=1)
    Button(tab_play, text='HighLow',command=lambda: view.game_window.highLowMainWindow(app,current_user)).grid(column=1,row=1)
    Button(tab_play, text='Roulette',command=lambda: view.game_window.rouletteMainWindow(app,current_user)).grid(column=0,row=2)
    Button(tab_play, text='Blackjack',command=lambda: view.game_window.blackjackMainWindow(app,current_user)).grid(column=1,row=2)
    Button(tab_play, text='Logout', command=lambda: userLogOut(app, current_user)).grid(column=0,row=5)

    ttk.Label(tab_pay, text='Mange your Payment').grid(column=0,row=1)
    ttk.Label(tab_pay, text='View your balance').grid(column=0,row=2)
    ttk.Label(tab_pay, text='Deposit money:').grid(column=0,row=3)
    ttk.Label(tab_pay, text='Withdraw money:').grid(column=0,row=4)
    ttk.Button(tab_pay, text='Deposit',command=lambda: validateMoney(deposit_money.get(),1,current_user)).grid(column=2,row=3)
    ttk.Button(tab_pay, text='Withdraw',command=lambda: validateMoney(withdraw_money.get(),2,current_user)).grid(column=2,row=4)
    Button(tab_pay, text='View', command=lambda: view.message_box.balanceMes(current_user)).grid(column=1,row=2)
    Button(tab_pay, text='Transaction', command=lambda: viewTransaction(current_user)).grid(column=2,row=2)
    Button(tab_pay, text='Logout', command=lambda: userLogOut(app, current_user)).grid(column=0,row=5)

    deposit_money = ttk.Entry(tab_pay)
    withdraw_money = ttk.Entry(tab_pay)

    deposit_money.grid(column=1,row=3)
    withdraw_money.grid(column=1,row=4)

    app.geometry("500x500")
    app.mainloop()

# Remove admin
# def adminMenuWindow(last_window, current_user):
#     closeWindow(last_window)

#     app = Tk()
#     app.title("Admin menu @Menu")
#     tabControl = ttk.Notebook(app)

#     tab_add = ttk.Frame(tabControl)
#     tab_select = ttk.Frame(tabControl)

#     tabControl.add(tab_add, text='Add game')
#     tabControl.add(tab_select, text='Select game')
#     tabControl.pack(expand=1, fill='both')

#     ttk.Label(tab_add, text='Add game in to Jade noi 888').grid(column=0,row=0)
#     #Button(tab_add, text='Back',command=lambda: selectRole(app,current_user)).grid(column=0,row=3)

#     ttk.Label(tab_select, text='Select game to make action').grid(column=0,row=0)
    
#     #Button(tab_select, text='Back',command=lambda: selectRole(app,current_user)).grid(column=0,row=3)

#     app.geometry("400x200")
#     app.mainloop()