from tkinter import *
from tkinter import ttk
from controller.login_controller import validateUser
from PIL import ImageTk, Image

def loginWindowMain():
    app = Tk()
    app.title('Casino Jade Noi 888 @Login')

    img = Image.open("../image/casinoHomepage.png")
    img_resize = img.resize((250,250))
    RPS_img = ImageTk.PhotoImage(img_resize)
    ttk.Label(app, image = RPS_img).grid(row=1,column=1,pady=(0,20))
    # bg_label.place(x = 0, y = 0)


    select_user = Label(text="Welcome to Jade Noi 888",foreground="red",font=18)
    select_user.grid(row=0,column=1,sticky = EW,pady=(20,20))

    user_name = Label(app, text= "Username :")
    user_name.grid(row=2,column=0,sticky = E,pady=(0,5),padx=(80,0))

    password = Label(app, text = "Password :")
    password.grid(row=3,column=0,sticky = E,pady=(0,5),padx=(80,0))

    user_name = Entry(app)
    password = Entry(app)

    user_name.grid(row=2,column=1,columnspan = 2)
    password.grid(row=3,column=1,columnspan = 2)

    login_button = Button(
        app, text="Login",bg='#25AEF3',height=1, width=20, command=lambda: validateUser(user_name.get(), password.get(), app))

    login_button.grid(row=4, column=1,pady=(30,15),columnspan = 3)

    app.geometry("500x500")
    app.mainloop()