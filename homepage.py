from tkinter import *
from ingredient import ilaunch
from Employee import elaunch
from bill import blaunch
from billList import bllaunch

# Creating window
root = Tk()
root.title("Homepage")
root.geometry("600x280")
root.config(bg="powderblue")

# Addint frames

topframe = Frame(root, bg="powderblue", width=150, height=150)
topframe.pack(side=TOP)

mainframe = Frame(root, bd=20)
mainframe.pack(pady=50, padx=50)

# Add varibles
welc = StringVar()


# defining the fns
def cbill():
    print("bill")
    root.destroy()
    blaunch()


def cingredients():
    print("Ingredient")
    root.destroy()
    ilaunch()


def cemployee():
    print("Employee")
    root.destroy()
    elaunch()


def cbillList():
    print("Bill list")
    root.destroy()
    bllaunch()


# Adding widgets

Label(topframe, text="Welcome!", font=('Times', 17, "bold italic"), bg="powderblue", fg="blue").grid(
    columnspan=10)

Bbill = Button(mainframe, text="Bill", bd=4, width=7, height=2, font=('Times', 12, "bold italic"), command=cbill).grid(
    row=2, column=2)

Bingredient = Button(mainframe, text="Ingredients", bd=4, width=7, height=2, font=('Times', 12, "bold italic"),
                     command=cingredients).grid(row=2, column=3)

Bemployee = Button(mainframe, text="Employees", bd=4, width=7, height=2, font=('Times', 12, "bold italic"),
                   command=cemployee).grid(row=2, column=4)

BbillList = Button(mainframe, text="Bills list", bd=4, width=7, height=2, font=('Times', 12, "bold italic"),
                   command=cbillList).grid(row=2, column=5)

root.mainloop()

