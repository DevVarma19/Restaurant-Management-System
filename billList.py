from tkinter import *
import sqlite3
from matplotlib import pyplot as plt
import os

date = {}

def bllaunch():
        #Creating root window
        root = Tk()
        root.geometry("750x700")
        root.title("List of Bills")
        root.config(bg="powder blue")

        #Add a grid
        topframe = Frame(root, bg="powder blue", width=150, height=100, padx=50, pady=50)
        topframe.pack(side=TOP)

        mainframe = Frame(root,bd=50)
        mainframe.pack()
        mainframe.config(bg="white")

        bottomframe = Frame(root,bg="powder blue",width=400,height=75,padx=50,pady=70)
        bottomframe.pack(side=BOTTOM)

        #Creating variables
        text = StringVar()
        text.set("")


        #Creating functions

        #defining fns for clearing the window
        def delete(frame):
            for widget in frame.winfo_children():
                widget.destroy()

        def colhead():
            Label(mainframe,text="OrderNo.",font=("Helvectica",14,"bold"),bg="white").grid(row=0,column=0)
            Label(mainframe, text="Date",font=("Helvectica",14,"bold"), bg="white").grid(row=0, column=2)
            Label(mainframe, text="Time",font=("Helvectica",14,"bold"), bg="white").grid(row=0, column=4)
            Label(mainframe, text="Amount",font=("Helvectica",14,"bold"), bg="white").grid(row=0, column=6)

        def display():
            delete(mainframe)
            print("Display Bills")
            colhead()
            conn = sqlite3.connect('Bills.db')
            cursor = conn.cursor()
            sql = '''SELECT * FROM bills'''
            results = cursor.execute(sql)
            print(results)
            bills = results.fetchall()
            print(bills)
            for index,bill in enumerate(bills):
                Label(mainframe,text=bill[0],bg="white",font=('times', 12, "italic")).grid(row = index+3,column=0)
                Label(mainframe,text=bill[1],bg="white",font=('times', 12, "italic")).grid(row = index+3,column=2)
                Label(mainframe,text=bill[2],bg="white",font=('times', 12, "italic")).grid(row = index+3,column=4)
                Label(mainframe,text=bill[3],bg="white",font=('times', 12, "italic")).grid(row = index+3,column=6)

        def getdata():
            # For getting the data
            conn = sqlite3.connect('Bills.db')
            cursor = conn.cursor()
            sql = '''SELECT * FROM bills'''
            results = cursor.execute(sql)
            bills = results.fetchall()
            print(bills)
            for bill in enumerate(bills):
                print(bill[1][1], bill[1][3])
                date[bill[1][1]] = date.get(bill[1][1], 0) + bill[1][3]
            print(date)

        def analysis():

            global date
            getdata()
            print("Analysis")

            dateL = []
            billL = []
            for i in date:
                dateL.append(i)
                billL.append(date[i])

            print(dateL)
            print(billL)


            plt.bar(dateL,billL,width=0.2)
            plt.title("Bill Analysis")
            plt.ylabel("Total Income")
            plt.xlabel("Date")
            plt.xticks(dateL)
            plt.show()

        def sumofbill():

            delete(mainframe)
            global date
            getdata()
            print(date)
            index = 2
            print("Per day sum")
            Label(mainframe,text="Date",font=('Helvetica', 14, "bold"),padx=10,bg="white").grid(row=1,column=0)
            Label(mainframe, text="Amount", font=('Helvetica', 14, "bold"),padx=10,bg="white").grid(row=1, column=2)
            Label(mainframe,text="(in INR)",font=('Helvetica',7),bg="white").grid(row=2,column=2)
            for i in date:
                Label(mainframe,text=i,bg="white",font=('times', 12, "italic")).grid(row=index+1,column=0)
                Label(mainframe,text=date[i],bg="white",font=('times', 12, "italic")).grid(row=index+1, column=2)
                index += 1

        def back():
            root.destroy()
            os.system('python homepage.py')

        #Adding Widgets

        Label(topframe,text="Bills List",font=('Times', 20, "bold"),bg="powderblue").grid(columnspan=8)

        Button(bottomframe,text="Display",font=('Helvetica', 14, "italic"),bd=4,command=display).pack(side=LEFT)
        Button(bottomframe,text="SumPerDay",font=('Helvetica', 14, "italic"),bd=4,command=sumofbill).pack(side=LEFT)
        Button(bottomframe, text="Analysis", font=('Helvetica', 14, "italic"), bd=4, command=analysis).pack(side=LEFT)
        Button(bottomframe, text="Back",font=('Helvetica', 14, "italic"),bd=4,command=back).pack(side=LEFT)

        root.mainloop()