from tkinter import *
import random
import time
from datetime import datetime
import sqlite3

equa = ""
sumall = 0
x = 0

def blaunch():
    #Creating main window
    root = Tk()
    root.title("Bill")
    root.geometry("1600x700")

    #Adding frames
    topframe = Frame(root,width=1600,height=50)
    topframe.pack(side=TOP)

    mf = Frame(root,width=900,height=700)
    mf.pack(side=LEFT)

    cf = Frame(root,width=400,height=700)
    cf.pack(side=RIGHT)

    #Time
    loctime = time.asctime(time.localtime(time.time()))#This gives entire details of local time

    #Header
    Label(topframe,font=('aria',25,'bold italic'),text="Bill Calculator",fg="steel blue").grid(row=0,column=0)
    Label(topframe,font=('aria',12),text="(with 18% GST)",fg="steel blue").grid(row=1,column=0)
    Label(topframe,font=('aria',15,'bold'),text=loctime,fg="steel blue",bd=10).grid(row=2,column=0)

    #CALCULATOR


    equation = StringVar()
    equa     = ""

    result = Entry(cf,font=('ariel' ,20,'bold'),text=equation,bd=5,justify="right",insertwidth=7)
    result.grid(columnspan=4)

    #Defining functions for calculator

    def btnPress(num):
        global equa
        equa = equa + str(num)
        equation.set(equa)

    def equalPress():
        global equa
        expResult = str(eval(equa))
        equation.set(expResult)
        equa = ""

    def Clear():
        global equa
        equa = ""
        equation.set("")

    #Adding widgets for calculator


    #ROW1

    B7 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="7",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(7))
    B7.grid(row=2,column=0)

    B8 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="8",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(8))
    B8.grid(row=2,column=1)

    B9 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="9",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(9))
    B9.grid(row=2,column=2)

    ADD = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,width=2,text="+",fg="black",bd=4,bg="powder blue",command=lambda :btnPress('+'))
    ADD.grid(row=2,column=3)

    #ROW2

    B6 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="6",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(6))
    B6.grid(row=3,column=0)

    B5 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="5",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(5))
    B5.grid(row=3,column=1)

    B4 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="4",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(4))
    B4.grid(row=3,column=2)

    SUB = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,width=2,text="-",fg="black",bd=4,bg="powder blue",command=lambda :btnPress("-"))
    SUB.grid(row=3,column=3)

    #ROW3

    B3 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="3",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(3))
    B3.grid(row=4,column=0)

    B2 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="2",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(2))
    B2.grid(row=4,column=1)

    B1 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="1",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(1))
    B1.grid(row=4,column=2)

    MUL = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,width=2,text="*",fg="black",bd=4,bg="powder blue",command=lambda :btnPress('*'))
    MUL.grid(row=4,column=3)

    #ROW4

    CLR = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="c",fg="black",bd=4,bg="powder blue",command=lambda:Clear())
    CLR.grid(row=5,column=0)

    B0 = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,text="0",fg="black",bd=4,bg="powder blue",command=lambda:btnPress(0))
    B0.grid(row=5,column=1)

    DOT = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,width=2,text=".",fg="black",bd=4,bg="powder blue",command=lambda:btnPress("."))
    DOT.grid(row=5,column=2)

    DIV = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,width=2,text="/",fg="black",bd=4,bg="powder blue",command=lambda :btnPress('/'))
    DIV.grid(row=5,column=3)

    #ROW5

    EQUAL = Button(cf,font=('ariel',20,'bold'),padx=16,pady=16,width=16,text="=",fg="black",bd=4,bg="powder blue",command=lambda :equalPress())
    EQUAL.grid(columnspan=4)


    #ITEM ENTRIES

    orderno = StringVar()
    Fries   = StringVar()
    Burger  = StringVar()
    Drinks  = StringVar()
    Pizza   = StringVar()
    Hotdogs = StringVar()
    Noodles = StringVar()
    Nachos  = StringVar()

    cost    = StringVar()
    tax     = StringVar()
    scharge = StringVar()
    Total   = StringVar()

    x= 20190
    sumall = 0

    #Defining functions for Menuframe



    def total():
        global x
        global sumall

        x =  random.randint(20190,201999)
        ref = str(x)
        orderno.set(ref)

        qof = int(Fries.get())
        qob = int(Burger.get())
        qod = int(Drinks.get())
        qop = int(Pizza.get())
        qoh = int(Hotdogs.get())
        qon = int(Nachos.get())
        qohn= int(Noodles.get())

        cof = qof * 45
        cob = qob * 50
        cod = qod * 30
        cop = qop * 90
        coh = qoh * 60
        con = qon * 70
        cohn= qohn* 80

        totalcost = cof + cob + cod + cop + coh + con + cohn
        Tax       = totalcost * (18/100)
        ser_charge= totalcost/99
        sumall    = totalcost + Tax + ser_charge

        costmeal  = "Rs.",str('%.2f'%totalcost)
        paidtax   = "Rs.",str('%.2f'%Tax)
        service   = "Rs.",str('%.2f'%ser_charge)
        overallbil= "Rs.",str('%.2f'%sumall)

        cost.set(costmeal)
        tax.set(paidtax)
        scharge.set(service)
        Total.set(overallbil)

    def savedb():
    # Saving the bill into database
        global sumall
        global x

        print("saving bill")
        conn = sqlite3.connect('Bills.db')
        cursor = conn.cursor()
        if not conn:
            print("Database error")
            return

        times = datetime.now()
        D = times.day
        M = times.month
        Y = times.year
        H = times.hour
        Min = times.minute

        date = "{D}/{M}/{Y}".format(D=D, M=M, Y=Y)
        time = "{H}:{m}".format(H=H, m=Min)
        amt = str('%2.f'%sumall)

        print(orderno,date, time, amt)

        sql = '''insert into bills
                                    (orderno,date,time,amount)
                                    values
                                    (:ono,:_date, :_time, :_amt)'''
        res = cursor.execute(sql, {'ono':x,'_date': date, '_time': time, '_amt': amt})
        conn.commit()
        cursor.close()
        if res:
            print("Saved successfully")
        else:
            print("Error! saving the bill")



    def bexit():
        root.destroy()
        savedb()

    def reset():
        orderno.set("")
        Fries .set("")
        Burger.set("")
        Drinks.set("")
        Pizza.set("")
        Hotdogs.set("")
        Noodles.set("")
        Nachos.set("")

        cost.set("")
        tax.set("")
        scharge.set("")
        Total.set("")



    #Adding widgets to MenuFrame

    Lorder = Label(mf,font=( 'aria' ,16, 'bold' ),text="Order No.",fg="steel blue",bd=10,anchor='w')
    Lorder.grid(row=0,column=0)
    Torder = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=orderno,bd=6,insertwidth=4,state='disabled',bg="powder blue",justify="right")
    Torder.grid(row=0,column=1)

    Lfries = Label(mf,font=( 'aria' ,16, 'bold' ),text="Fries",fg="steel blue",bd=10,anchor='w')
    Lfries.grid(row=1,column=0)
    Tfries = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=Fries,bd=6,insertwidth=4,bg="powder blue",justify="right")
    Tfries.grid(row=1,column=1)

    Lburger = Label(mf,font=( 'aria' ,16, 'bold' ),text="Burger",fg="steel blue",bd=10,anchor='w')
    Lburger.grid(row=2,column=0)
    Tburger = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=Burger,bd=6,insertwidth=4,bg="powder blue",justify="right")
    Tburger.grid(row=2,column=1)

    Lpizza = Label(mf,font=( 'aria' ,16, 'bold' ),text="Pizza",fg="steel blue",bd=10,anchor='w')
    Lpizza.grid(row=3,column=0)
    Tpizza = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=Pizza,bd=6,insertwidth=4,bg="powder blue",justify="right")
    Tpizza.grid(row=3,column=1)

    LHotdogs = Label(mf,font=( 'aria' ,16, 'bold' ),text="HotDogs",fg="steel blue",bd=10,anchor='w')
    LHotdogs.grid(row=4,column=0)
    THotdogs = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=Hotdogs,bd=6,insertwidth=4,bg="powder blue",justify="right")
    THotdogs.grid(row=4,column=1)

    LNoodels = Label(mf,font=( 'aria' ,16, 'bold' ),text="Noodles",fg="steel blue",bd=10,anchor='w')
    LNoodels.grid(row=5,column=0)
    TNoodels = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=Noodles,bd=6,insertwidth=4,bg="powder blue",justify="right")
    TNoodels.grid(row=5,column=1)

    Ldrinks = Label(mf,font=( 'aria' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
    Ldrinks.grid(row=0,column=2)
    Tdrinks = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=Drinks,bd=6,insertwidth=4,bg="powder blue",justify="right")
    Tdrinks.grid(row=0,column=3)

    Lnachos = Label(mf,font=( 'aria' ,16, 'bold' ),text="Nachos",fg="steel blue",bd=10,anchor='w')
    Lnachos.grid(row=1,column=2)
    Tnachos = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=Nachos,bd=6,insertwidth=4,bg="powder blue",justify="right")
    Tnachos.grid(row=1,column=3)

    Lcost  = Label(mf,font=( 'aria' ,16, 'bold' ),text="Cost",fg="steel blue",bd=10,anchor='w')
    Lcost.grid(row=2,column=2)
    Tcost = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=cost,state='disabled',bd=6,insertwidth=4,bg="powder blue",justify="right")
    Tcost.grid(row=2,column=3)

    Ltax = Label(mf,font=( 'aria' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
    Ltax.grid(row=3,column=2)
    Ttax = Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=tax,state='disabled',bd=6,insertwidth=4,bg="powder blue",justify="right")
    Ttax.grid(row=3,column=3)

    Lscharge = Label(mf,font=( 'aria' ,16, 'bold' ),text="ServiceCharges",fg="steel blue",bd=10,anchor='w')
    Lscharge.grid(row=4,column=2)
    Tscharge= Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=scharge,state='disabled',bd=6,insertwidth=4,bg="powder blue",justify="right")
    Tscharge.grid(row=4,column=3)

    Ltotal = Label(mf,font=( 'aria' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
    Ltotal.grid(row=5,column=2)
    Ttotal= Entry(mf,font=( 'aria' ,16, 'bold' ),textvariable=Total,state='disabled',bd=6,insertwidth=4,bg="powder blue",justify="right")
    Ttotal.grid(row=5,column=3)

    #Adding buttons at the last

    Label(mf).grid(columnspan=8)
    Label(mf).grid(columnspan=8)

    BTOTAL = Button(mf,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=total)
    BTOTAL.grid(row=8,column=1)

    BRESET = Button(mf,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
    BRESET.grid(row=8,column=2)

    BEXIT = Button(mf,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="powder blue",command=bexit)
    BEXIT.grid(row=8,column=3)


    #Adding a Price window

    def price():
        pw = Tk()
        pw.geometry("450x300")
        pw.title("Price List")

        litem = Label(pw,font=('aria',16,'bold'),text="ITEM",fg="black",bd=5)
        litem.grid(row=0,column=0)

        l     = Label(pw,font=('aria',16,'bold'),text="__________",fg="white",anchor='w')
        l.grid(row=0,column=2)

        lprice= Label(pw,font=('aria',16,'bold'),text="PRICE",fg="black",bd=5)
        lprice.grid(row=0,column=3)

        lburger = Label(pw, font=('aria', 16, 'bold'), text="Burger", fg="steel blue", bd=5)
        lburger.grid(row=1, column=0)

        lbprice = Label(pw, font=('aria', 16, 'bold'), text="50", fg="steel blue", bd=5)
        lbprice.grid(row=1, column=3)

        lfries = Label(pw, font=('aria', 16, 'bold'), text="Fries", fg="steel blue", bd=5)
        lfries.grid(row=2, column=0)

        lfprice = Label(pw, font=('aria', 16, 'bold'), text="45", fg="steel blue", bd=5)
        lfprice.grid(row=2, column=3)

        ldrinks = Label(pw, font=('aria', 16, 'bold'), text="Drinks", fg="steel blue", bd=5)
        ldrinks.grid(row=3, column=0)

        ldprice = Label(pw, font=('aria', 16, 'bold'), text="30", fg="steel blue", bd=5)
        ldprice.grid(row=3, column=3)

        lpizza= Label(pw, font=('aria', 16, 'bold'), text="Pizza", fg="steel blue", bd=5)
        lpizza.grid(row=4, column=0)

        lpprice = Label(pw, font=('aria', 16, 'bold'), text="90", fg="steel blue", bd=5)
        lpprice.grid(row=4, column=3)

        lhotdogs = Label(pw, font=('aria', 16, 'bold'), text="Hot Dogs", fg="steel blue", bd=5)
        lhotdogs.grid(row=5, column=0)

        lbprice = Label(pw, font=('aria', 16, 'bold'), text="60", fg="steel blue", bd=5)
        lbprice.grid(row=5, column=3)

        lnachos = Label(pw, font=('aria', 16, 'bold'), text="Nachos", fg="steel blue", bd=5)
        lnachos.grid(row=6, column=0)

        lbprice = Label(pw, font=('aria', 16, 'bold'), text="70", fg="steel blue", bd=5)
        lbprice.grid(row=6, column=3)

        lburger = Label(pw, font=('aria', 16, 'bold'), text="Hakka Noodles", fg="steel blue", bd=5)
        lburger.grid(row=7, column=0)

        lbprice = Label(pw, font=('aria', 16, 'bold'), text="80", fg="steel blue", bd=5)
        lbprice.grid(row=7, column=3)

    #Adding price button
    BPRICE =Button(mf,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
    BPRICE.grid(row=8, column=0)

    root.mainloop()
