from tkinter import *
from tkinter import ttk
from controller.user_controller import removeUserFromList
from controller.account_controller import accountGetBalance, accountDeposit, accountWithdraw
from controller.transaction_controller import showTransactionLog
import view.game_window
import view.message_box 
from PIL import ImageTk, Image


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

def viewTransaction(current_user):
    app = Tk()
    app.title("Transaction")
    scrollbar = Scrollbar(app, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)

    transaction_list = showTransactionLog(current_user)
    i = 0

    l1 = Listbox(app, height=50, width=150, bg='white',yscrollcommand=scrollbar.set)
    l1.pack(side=LEFT,padx=15) 
    for transaction in transaction_list:
        print(transaction.displayTransaction())
        l1.insert(END, transaction.displayTransaction())
        i += 1
    scrollbar.config(command = l1.yview)
    app.geometry("500x500")
    app.mainloop()



def userMenuWindow(last_window, current_user):
    closeWindow(last_window)

    app = Tk()


    app.title("Main menu")
    tabControl = ttk.Notebook(app)

    tab_play = ttk.Frame(tabControl)
    tab_pay = ttk.Frame(tabControl)

    tabControl.add(tab_play, text='Play')
    tabControl.add(tab_pay, text='Account')
    tabControl.pack(expand=1, fill="both")

    img = Image.open("../image/RPS.png")
    img_resize = img.resize((177,100))
    RPS_img = ImageTk.PhotoImage(img_resize)
    ttk.Label(tab_play, image = RPS_img).grid(column = 1,row = 1,sticky = W,pady=(0,15),columnspan = 2)
    
    img = Image.open("../image/HL.png")
    img_resize = img.resize((177,100))
    HL_img = ImageTk.PhotoImage(img_resize)
    ttk.Label(tab_play, image = HL_img).grid(column = 1,row = 2,sticky = W,pady=(0,15),columnspan = 2)

    img = Image.open("../image/Roulette.png")
    img_resize = img.resize((177,100))
    Roulette_img = ImageTk.PhotoImage(img_resize)
    ttk.Label(tab_play, image = Roulette_img).grid(column = 1,row = 3,sticky = W,pady=(0,15),columnspan = 2)

    img = Image.open("../image/blackJack.png")
    img_resize = img.resize((177,100))
    blackJack_img = ImageTk.PhotoImage(img_resize)
    ttk.Label(tab_play, image = blackJack_img).grid(column = 1,row = 4,sticky = W,pady=(0,15),columnspan = 2)

    ttk.Label(tab_play, text='Games in Jade Noi 888',foreground="#1A57FF",font=14).grid(column=0,row=0,pady=(10,40),columnspan = 2)
    Button(tab_play, text='RPS',bg='#25AEF3',height=1, width=10,command=lambda: view.game_window.rpsMainWindow(app,current_user)).grid(column=0,row=1,pady=(0,15),padx=(30,30),sticky = W)
    Button(tab_play, text='HighLow',bg='#25AEF3',height=1, width=10,command=lambda: view.game_window.highLowMainWindow(app,current_user)).grid(column=0,row=2,pady=(0,15),padx=(30,30),sticky = W)
    Button(tab_play, text='Roulette',bg='#25AEF3',height=1, width=10,command=lambda: view.game_window.rouletteMainWindow(app,current_user)).grid(column=0,row=3,pady=(0,15),padx=(30,30),sticky = W)
    Button(tab_play, text='Blackjack',bg='#25AEF3',height=1, width=10,command=lambda: view.game_window.blackjackMainWindow(app,current_user)).grid(column=0,row=4,pady=(0,15),padx=(30,30),sticky = W)
    Button(tab_play, text='Logout', bg='black', fg='white', height=1, width=10, command=lambda: userLogOut(app, current_user)).grid(column=0,row=5,pady=(40,0),padx=(10,0),sticky = W)

    ttk.Label(tab_pay, text='Manage your Payment',foreground="green",font=14).grid(column=0,row=0,pady=(10,40),columnspan = 2)
    ttk.Label(tab_pay, text='Account balance:').grid(column=0,row=1,pady=(0,20),padx=(10,10),sticky = W)
    ttk.Label(tab_pay, text='Deposit money:').grid(column=0,row=4,padx=(10,5),sticky = W)
    ttk.Label(tab_pay, text='Withdraw money:').grid(column=0,row=5,padx=(10,5),sticky = W)
    ttk.Button(tab_pay, text='Deposit',command=lambda: validateMoney(deposit_money.get(),1,current_user)).grid(column=2,row=4,padx=(5,5))
    ttk.Button(tab_pay, text='Withdraw',command=lambda: validateMoney(withdraw_money.get(),2,current_user)).grid(column=2,row=5,padx=(5,5))
    Button(tab_pay, text='view money balance',bg='green', fg='white', command=lambda: view.message_box.balanceMes(current_user)).grid(column=1,row=1,sticky = W)
    Button(tab_pay, text='transaction history',bg='green', fg='white', command=lambda: viewTransaction(current_user)).grid(column=1,row=2,sticky = W,pady=(0,20),)
    Button(tab_pay, text='Logout', bg='black', fg='white', height=1, width=10, command=lambda: userLogOut(app, current_user)).grid(column=0,row=6,pady=(40,0),padx=(10,0),sticky = W)

    deposit_money = ttk.Entry(tab_pay)
    withdraw_money = ttk.Entry(tab_pay)

    deposit_money.grid(column=1,row=4)
    withdraw_money.grid(column=1,row=5)

    app.geometry("400x680")
    app.mainloop()