from tkinter import *
from tkinter import ttk
from view.user_action_window import play_window, pay_window
from view.admin_action_window import add_game_window, select_game_window

def select_role():
    app = Tk()
    app.title("Select role @Menu")

    user_button = Button(app, text='User',
                        command = lambda: user_menu_window())
    admin_button = Button(app, text='Admin',
                        command = lambda: admin_menu_window())
    
    user_button.grid(row=0,column=0)
    admin_button.grid(row=0,column=1)
    
    app.geometry("400x200")
    app.mainloop()

def user_menu_window():
    app = Tk()
    app.title("User menu @Menu")

    Label(app, text='Choose action').grid(row=0,column=0)

    play_button = Button(app, text='Play',
                        command=lambda: play_window())
    pay_button = Button(app, text='Manage payment',
                        command=lambda: pay_window())
    
    play_button.grid(row=1,column=0)
    pay_button.grid(row=1,column=1)

    app.geometry("400x200")
    app.mainloop()

def admin_menu_window():
    app = Tk()
    app.title("Admin menu @Menu")

    Label(app, text='Choose action').grid(row=0,column=0)

    add_button = Button(app, text='Add',
                        command=lambda: add_game_window())
    select_button = Button(app, text='Select game',
                        command=lambda: select_game_window())
    
    add_button.grid(row=1,column=0)
    select_button.grid(row=1,column=1)

    app.geometry("400x200")
    app.mainloop()