from tkinter import *
import sqlite3
import os
from tkinter import messagebox

#Creating Window
root = Tk()
root.title("Login")
root.geometry('600x600')
root.config(bg="white")

#Add a frame

topframe = Frame(root,bg="white",width=150,height=150,padx=100,pady=100)
topframe.pack(side=TOP)

mainframe = Frame(root,bd=20,bg="powderblue",width=150,height=150,padx=150,pady=110)
mainframe.pack()

#Creating Variables
username = StringVar()
password = StringVar()
msg      = StringVar()
name     = StringVar()

#Defining the functions
def checklogin():
    uname = username.get()
    pword = password.get()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    sql = "select * from users"
    results = cursor.execute(sql)
    users = results.fetchall()
    print(users)

    namer  = users[0][0]
    Unamer = users[0][1]
    Pwordr = users[0][2]

    if uname == Unamer and pword == Pwordr:
        #uname = manager #pword = hello123
        text = "Welcome " + namer;
        msg.set(text)

        w = Message(mainframe,textvariable = msg,font=("Helvetica", "9"))
        w.grid(columnspan=5)

        root.destroy()
        os.system('python homepage.py')
    else:
        messagebox.showerror("Invalid!","Invalid Credentials!!")


#Adding Widgets
Euser = Entry(mainframe,textvariable = username,bd=6,bg="white",font=("Helvetica", "12")) #Username
Epass = Entry(mainframe,textvariable = password,show="*",bd=6,bg="white",font=("Helvetica", "12")) #Password


Label(topframe,text = "Restaurant Management System",font=('Times', 17,"bold italic"),bg="white",fg="blue").grid(columnspan=10)
Label(mainframe,text = "Username",font=('Times', 12,"bold italic"),bg="powderblue").grid(row=2,column=1)
Label(mainframe,text = "Password",font=('Times', 12,"bold italic"),bg="powderblue").grid(row=3,column=1)

Euser.grid(row=2,column=3)
Epass.grid(row=3,column=3)

Blogin = Button(mainframe,text="Login",bd=4,width=7,height=1,font=('Times', 12,"bold italic"),command = checklogin).grid(columnspan=10)

root.mainloop()

#state="disabled"