from tkinter import *
from tkinter import ttk
from controller.login_controller import validateUser

def loginWindowMain():
    app = Tk()
    app.title('Casino Jade Noi 888 @Login')

    select_user = Label(text="เจ้าชื่อหยัง?",font=20)
    select_user.grid(row=0,column=1)

    Label(app, text= "User Name").grid(row=1)
    Label(app, text = "Password").grid(row=2)

    user_name = Entry(app)
    password = Entry(app)

    user_name.grid(row=1, column=1)
    password.grid(row=2, column=1)
    login_button = Button(
        app, text="Login", command=lambda: validateUser(user_name.get(), password.get(), app))

    login_button.grid(row=3, column=1)

    app.geometry("400x200")
    app.mainloop()