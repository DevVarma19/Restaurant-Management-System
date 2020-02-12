from tkinter import *
import sqlite3
import os

def elaunch():
        #Creating window
        root = Tk()
        root.geometry("850x750")
        root.title("Employee List")
        root.config(bg="powderblue")

        #Adding grid
        topframe = Frame(root, bg="powderblue", width=150, height=150, padx=50, pady=50)
        topframe.pack(side=TOP)

        mainframe = Frame(root, bd=50)
        mainframe.pack()
        mainframe.config(bg="white")

        bottomframe = Frame(root, bg="powderblue", width=400, height=100, padx=50, pady=50)
        bottomframe.pack(side=BOTTOM)

        secondbf = Frame(root, bg="powderblue", width=50, height=50, padx=25, pady=12)
        secondbf.pack(side=BOTTOM)

        #creating variables
        global i
        i = 1
        addname  = StringVar()
        addname.set('Name')
        addage   = IntVar()
        adddesig = StringVar()
        adddesig.set('Designation')
        text = StringVar()

        #defining functions

        def colhead():

            Label(mainframe, text="Name",font=('times',15,'bold'),fg="blue" ,bg="white").grid(row=1, column=0)
            Label(mainframe, text="Age",font=('times',15,'bold'),fg="blue", bg="white").grid(row=1, column=1)
            Label(mainframe, text="Designation",font=('times',15,'bold'),fg="blue", bg="white").grid(row=1, column=2)
            Label(mainframe,bg="white").grid(columnspan=8)


        def display():
            print("Display Employees")
            conn = sqlite3.connect('employee.db')
            cursor = conn.cursor()
            sql = '''SELECT * FROM employees'''
            results = cursor.execute(sql)
            items = results.fetchall()
            global i
            if i == 1:
                colhead()
                i += 1
            for index, item in enumerate(items):
                Label(mainframe, text=item[0], bg="white").grid(row=index + 3, column=0)
                Label(mainframe, text=item[1], bg="white").grid(row=index + 3, column=1)
                Label(mainframe, text=item[2], bg="white").grid(row=index + 3, column=2)
            text.set("")

        def add():
            print("Add")
            aname = addname.get()
            aage = addage.get()
            adesig = adddesig.get()

            conn = sqlite3.connect('employee.db')
            cursor = conn.cursor()
            sql = '''insert into employees
                                            (name,age,design)
                                            values
                                            (:us_name, :us_age, :us_design)'''
            res = cursor.execute(sql, {'us_name': aname, 'us_age': aage, 'us_design': adesig})
            conn.commit()
            cursor.close()
            if (res):
                text.set("Added successfully")
                print("Added successfully")
                w = Label(root, textvariable=text,bg="powder blue").pack(side=BOTTOM)

        def back():
            root.destroy()
            os.system('python homepage.py')

        #Add widgets

        Label(topframe, text="EMPLOYEE LIST", font=('Times', 16, "bold"), bg="powderblue").grid(columnspan=8)

        badd = Button(bottomframe, text="Add", width=8, height=1, bd=4,font=('Times', 12, "bold italic"), command=add).pack(
            side=LEFT)

        aitem = Entry(bottomframe,textvariable=addname,bd=6,bg="white",font=("Helvetica", 12)).pack(side=LEFT)

        aage  = Entry(bottomframe,textvariable=addage,bd=6,bg="white",font=("Helvectica",12)).pack(side=LEFT)

        adesig = Entry(bottomframe,textvariable=adddesig,bd=6,bg="white",font=("Helvetica", 12)).pack(side=LEFT)

        bback = Button(bottomframe, text="Back", width=8, height=1, bd=4 ,font=('Times', 12, "bold italic"),
                      command=back).pack(side=LEFT)

        bdisplay = Button(secondbf, text="Display", width=8, height=1, bd=4, font=('Times', 12, "bold italic"),
                          command=display).pack(side=BOTTOM)

        root.mainloop()


