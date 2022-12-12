from tkinter import *
from tkinter import ttk
from controller.user_controller import removeUserFromList
from view.game_window import rpsMainWindow, highLowMainWindow, rouletteMainWindow, spinMainWindow, slotMainWindow, blackjackMainWindow
from controller.account_controller import accountGetBalance
from view.game_window import rpsMainWindow

def closeWindow(app):
    app.destroy()

def userLogOut(app, current_user):
    removeUserFromList(current_user)
    app.destroy()

def getBalance(current_user):
    print("current balance",accountGetBalance(current_user))

def selectRole(last_window, current_user):
    closeWindow(last_window)
    app = Tk()
    app.title("Select role @Menu")

    user_button = Button(app, text='User',
                        command=lambda: userMenuWindow(app, current_user))
    admin_button = Button(app, text='Admin',
                        command=lambda: adminMenuWindow(app, current_user))
    logout_button = Button(app, text='Logout',
                        command=lambda: userLogOut(app, current_user))
    
    user_button.grid(row=0,column=0)
    admin_button.grid(row=0,column=1)
    logout_button.grid(row=0,column=2)

    app.geometry("400x200")
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
    Button(tab_play, text='RPS',command=lambda: rpsMainWindow(app,current_user)).grid(column=0,row=1)
    Button(tab_play, text='HighLow',command=lambda: highLowMainWindow(app,current_user)).grid(column=1,row=1)
    Button(tab_play, text='Roulette',command=lambda: rouletteMainWindow(app,current_user)).grid(column=2,row=1)
    Button(tab_play, text='Spin',command=lambda: spinMainWindow(app,current_user)).grid(column=0,row=2)
    Button(tab_play, text='Slot',command=lambda: slotMainWindow(app,current_user)).grid(column=1,row=2)
    Button(tab_play, text='Blackjack',command=lambda: blackjackMainWindow(app,current_user)).grid(column=2,row=2)
    Button(tab_play, text='Back',command=lambda: selectRole(app,current_user)).grid(column=0,row=5)

    ttk.Label(tab_pay, text='Mange your Payment').grid(column=0,row=1)
    Button(tab_pay, text='Back',command=lambda: selectRole(app,current_user)).grid(column=0,row=3)

    app.geometry("300x300")
    app.mainloop()

def adminMenuWindow(last_window, current_user):
    closeWindow(last_window)

    app = Tk()
    app.title("Admin menu @Menu")
    tabControl = ttk.Notebook(app)

    tab_add = ttk.Frame(tabControl)
    tab_select = ttk.Frame(tabControl)

    tabControl.add(tab_add, text='Add game')
    tabControl.add(tab_select, text='Select game')
    tabControl.pack(expand=1, fill='both')

    ttk.Label(tab_add, text='Add game in to Jade noi 888').grid(column=0,row=0)
    Button(tab_add, text='Back',command=lambda: selectRole(app,current_user)).grid(column=0,row=3)

    ttk.Label(tab_select, text='Select game to make action').grid(column=0,row=0)
    Button(tab_select, text='Back',command=lambda: selectRole(app,current_user)).grid(column=0,row=3)

    app.geometry("400x200")
    app.mainloop()