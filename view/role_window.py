from tkinter import *
from tkinter import ttk

def close_window(app):
    app.destroy()

def select_role(last_window):
    close_window(last_window)
    app = Tk()
    app.title("Select role @Menu")

    user_button = Button(app, text='User',
                        command = lambda: user_menu_window(app))
    admin_button = Button(app, text='Admin',
                        command = lambda: admin_menu_window(app))
    
    user_button.grid(row=0,column=0)
    admin_button.grid(row=0,column=1)
    
    app.geometry("400x200")
    app.mainloop()

def user_menu_window(last_window):
    close_window(last_window)

    app = Tk()
    app.title("User menu @Menu")
    tabControl = ttk.Notebook(app)

    tab_play = ttk.Frame(tabControl)
    tab_pay = ttk.Frame(tabControl)

    tabControl.add(tab_play, text='Play')
    tabControl.add(tab_pay, text='Pay')
    tabControl.pack(expand=1, fill="both")

    ttk.Label(tab_play, text='Let play game in Jade Noi 888').grid(column=0,row=0)
    Button(tab_play, text='Back',command=lambda: select_role(app)).grid(column=0,row=3)

    ttk.Label(tab_pay, text='Mange your Payment').grid(column=0,row=1)
    Button(tab_pay, text='Back',command=lambda: select_role(app)).grid(column=0,row=3)

    app.geometry("300x300")
    app.mainloop()

def admin_menu_window(last_window):
    close_window(last_window)

    app = Tk()
    app.title("Admin menu @Menu")
    tabControl = ttk.Notebook(app)

    tab_add = ttk.Frame(tabControl)
    tab_select = ttk.Frame(tabControl)

    tabControl.add(tab_add, text='Add game')
    tabControl.add(tab_select, text='Select game')
    tabControl.pack(expand=1, fill='both')

    ttk.Label(tab_add, text='Add game in to Jade noi 888').grid(column=0,row=0)
    Button(tab_add, text='Back',command=lambda: select_role(app)).grid(column=0,row=3)

    ttk.Label(tab_select, text='Select game to make action').grid(column=0,row=0)
    Button(tab_select, text='Back',command=lambda: select_role(app)).grid(column=0,row=3)

    app.geometry("400x200")
    app.mainloop()