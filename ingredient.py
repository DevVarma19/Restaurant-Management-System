from tkinter import *
import sqlite3
import os

def ilaunch():
        #Creating Window
        root = Tk()
        root.title("Ingredient List")
        root.geometry('700x600')
        root.config(bg="powderblue")

        #Add a grid
        topframe = Frame(root, bg="powderblue", width=150, height=150, padx=25, pady=50)
        topframe.pack(side=TOP)

        mainframe = Frame(root,bd=25)
        mainframe.pack()
        mainframe.config(bg="white")

        bottomframe = Frame(root,bg="powderblue",width=400,height=50,padx=50,pady=50)
        bottomframe.pack(side=BOTTOM)


        #creating variables
        global i
        i = 1
        ingredients = StringVar()
        additem     = StringVar()
        addqty      = IntVar()
        text        = StringVar()
        text.set("")
        #defining functions
        def colhead():
            Label(mainframe, text="Item",fg="blue" ,bg="white",font=('aria',16,'bold')).grid(row=1, column=0)
            Label(mainframe, text="QTY",fg="blue",bg="white",font=('aria',14,'bold')).grid(row=1, column=1)
            Label(mainframe, bg="white").grid(columnspan=8)
        def display():
            print("Display ingredients")
            conn = sqlite3.connect('ingredient.db')
            cursor = conn.cursor()
            sql = '''SELECT * FROM items'''
            results = cursor.execute(sql)
            items = results.fetchall()

            global i
            if i == 1:
                colhead()
                i += 1
            for index,item in enumerate(items):
                Label(mainframe,text=item[0],bg="white").grid(row = index+3,column = 0)
                Label(mainframe,text=item[1],bg="white").grid(row = index+3,column = 1)

        def update():
            print("update")
            type = additem.get()
            qty = addqty.get()

            conn = sqlite3.connect('ingredient.db')
            cursor = conn.cursor()
            sql = '''update items set quantity = {0} where type = '{1}' '''.format(qty,type)
            print(sql)
            res = cursor.execute(sql)
            conn.commit()
            cursor.close()
            if(res):
                text.set("Updated successfully")
                print("Added successfully")
                w = Label(root,textvariable = text).pack(side=BOTTOM)

        def back():

            root.destroy()
            os.system('python homepage.py')



        #adding widgets
        Label(topframe, text="INVENTORY", font=('Times', 16, "bold"), bg="powderblue").grid(columnspan=8)

        bdisplay = Button(bottomframe,text="View",width=8,height=1,font=('Times', 12,"bold italic"),command=display).pack(side=LEFT)

        aitem = Entry(bottomframe,textvariable=additem,bd=6,bg="white",font=("Helvetica", 12)).pack(side=LEFT)

        aqty  = Entry(bottomframe,textvariable=addqty,bd=6,bg="white",font=("Helvectica",12)).pack(side=LEFT)

        badd  = Button(bottomframe,text="Update",width=8,height=1,font=('Times', 12,"bold italic"),command=update).pack(side=LEFT)

        bexit = Button(bottomframe,text="Back",width=8,height=1,font=('Times', 12,"bold italic"),command=back).pack(side=LEFT)

        root.mainloop()
