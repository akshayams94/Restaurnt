from tkinter import*
import random
import time
 
root = Tk()
root.geometry("1600x700+0+0")
root.title("Akshaya Restaurant Management System")


Tops = Frame(root,bg="white",width = 1600,height=50,relief=SUNKEN)
Tops.pack(side=TOP)
 
f1 = Frame(root,width = 900,height=700,relief=SUNKEN)
f1.pack(side=LEFT)
 
f2 = Frame(root ,width = 400,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Akshaya Restaurant Management System",bg="pink",fg="white",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="black",anchor=W)
lblinfo.grid(row=1,column=0)
 
#---------------Calculator------------------
text_Input=StringVar()
operator =""
 
txtdisplay = Entry(f2,font=('ariel' ,20,'bold'), textvariable=text_Input , bd=5 ,insertwidth=7 ,bg="white",justify='left')
txtdisplay.grid(columnspan=4)
 
def  btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)
 
def clrdisplay():
    global operator
    operator=""
    text_Input.set("")
 
def eqals():
    global operator
    sumup=str(eval(operator))
 
    text_Input.set(sumup)
    operator = ""
 
def Ref():
    x=random.randint(12980, 50876)
    randomRef = str(x)
    ado.set(randomRef)
 
    star =float(start.get())
    vegcom= float(vegcomb.get())
    meatcom= float(meatcomb.get())
    kidscom= float(kidscomb.get())
    desert= float(desertpack.get())
    drink= float(drinkset.get())
 
    starprice = star*7
    vegcomprice = vegcom*15
    meatcomprice = meatcom*23
    kidscomprice = kidscom*12
    desertprice = desert*8
    drinksprice = drink*7
 
    dinnercost = str('%.2f'% (starprice +  vegcomprice + meatcomprice + kidscomprice + desertprice + drinksprice)),"€"
    PayTax=((starprice +  vegcomprice + meatcomprice + kidscomprice +  desertprice + drinksprice)*0.33)
    Totalcost=(starprice +  vegcomprice + meatcomprice + kidscomprice  + desertprice + drinksprice)
    Ser_Charge=((starprice +  vegcomprice + meatcomprice + kidscomprice + desertprice + drinksprice)/99)
    Service=str('%.2f'% Ser_Charge),"€"
    OverAllCost=str( PayTax + Totalcost + Ser_Charge),"€"
    PaidTax=str('%.2f'% PayTax),"€"
 
    Service_Charge.set(Service)
    cost.set(dinnercost)
    Tax.set(PaidTax)
    Subtotal.set(dinnercost)
    Total.set(OverAllCost)
 
 
def qexit():
    root.destroy()
 
def reset():
    ado.set("")
    start.set("")
    vegcomb.set("")
    meatcomb.set("")
    kidscomb.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    drinkset.set("")
    Tax.set("")
    cost.set("")
    desertpack.set("")
 
 
btn7=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="7",bg="black", command=lambda: btnclick(7) )
btn7.grid(row=2,column=0)
 
btn8=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="8",bg="black", command=lambda: btnclick(8) )
btn8.grid(row=2,column=1)
 
btn9=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="9",bg="black", command=lambda: btnclick(9) )
btn9.grid(row=2,column=2)
 
Addition=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="+",bg="black", command=lambda: btnclick("+") )
Addition.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------
btn4=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="4",bg="black", command=lambda: btnclick(4) )
btn4.grid(row=3,column=0)
 
btn5=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="5",bg="black", command=lambda: btnclick(5) )
btn5.grid(row=3,column=1)
 
btn6=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="6",bg="black", command=lambda: btnclick(6) )
btn6.grid(row=3,column=2)
 
Substraction=Button(f2,padx=13,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="-",bg="black", command=lambda: btnclick("-") )
Substraction.grid(row=3,column=3)
#-----------------------------------------------------------------------------------------------
btn1=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="1",bg="black", command=lambda: btnclick(1) )
btn1.grid(row=4,column=0)
 
btn2=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="2",bg="black", command=lambda: btnclick(2) )
btn2.grid(row=4,column=1)
 
btn3=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="3",bg="black", command=lambda: btnclick(3) )
btn3.grid(row=4,column=2)
 
multiply=Button(f2,padx=13,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="*",bg="black", command=lambda: btnclick("*") )
multiply.grid(row=4,column=3)
#------------------------------------------------------------------------------------------------
btn0=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="0",bg="black", command=lambda: btnclick(0) )
btn0.grid(row=5,column=0)
 
btnc=Button(f2,padx=10,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="c",bg="black", command=clrdisplay)
btnc.grid(row=5,column=1)
 
btnequal=Button(f2,padx=10,pady=16,bd=4,width = 16, fg="red", font=('ariel', 20 ,'bold'),text="=",bg="black",command=eqals)
btnequal.grid(columnspan=4)
 
Decimal=Button(f2,padx=13,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text=".",bg="black", command=lambda: btnclick(".") )
Decimal.grid(row=5,column=2)
 
Division=Button(f2,padx=13,pady=16,bd=4, fg="red", font=('ariel', 20 ,'bold'),text="/",bg="black", command=lambda: btnclick("/") )
Division.grid(row=5,column=3)
status = Label(f2,font=('aria', 15, 'bold'),width = 16, text="Cisco Calculator",bd=2,relief=SUNKEN)
status.grid(row=7,columnspan=3)
 
#---------------------------------------------------------------------------------------
ado = StringVar()
start = StringVar()
vegcomb = StringVar()
meatcomb = StringVar()
kidscomb = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
drinkset = StringVar()
Tax = StringVar()
cost = StringVar()
desertpack = StringVar()
 
 
lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="red",bd=10,anchor='w')
lblreference.grid(row=0,column=0)
txtreference = Entry(f1, font=('ariel' ,16,'bold'), textvariable=ado, bd=6, insertwidth=4, bg="white", justify='right')
txtreference.grid(row=0,column=1)
 
lblmanok = Label(f1, font=('aria' , 16, 'bold'), text="starters", fg="green", bd=10, anchor='w')
lblmanok.grid(row=1, column=0)
txtmanok = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=start, bd=6, insertwidth=4, bg="white", justify='right')
txtmanok.grid(row=1, column=1)
 
lblbaboy = Label(f1, font=('aria' , 16, 'bold'), text="veg combo", fg="green", bd=10, anchor='w')
lblbaboy.grid(row=2, column=0)
txtbaboy = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=vegcomb, bd=6, insertwidth=4, bg="white", justify='right')
txtbaboy.grid(row=2, column=1)
 
 
lblhipon = Label(f1, font=('aria' , 16, 'bold'), text="meat combo", fg="green", bd=10, anchor='w')
lblhipon.grid(row=3, column=0)
txthipon = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=meatcomb, bd=6, insertwidth=4, bg="white", justify='right')
txthipon.grid(row=3, column=1)
 
lblkarikari = Label(f1, font=('aria' , 16, 'bold'), text="kids combo", fg="green", bd=10, anchor='w')
lblkarikari.grid(row=4, column=0)
txtkarikari = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=kidscomb, bd=6, insertwidth=4, bg="white", justify='right')
txtkarikari.grid(row=4, column=1)
 
lblpaksiw = Label(f1, font=('aria' , 16, 'bold'), text="Dessert", fg="green", bd=10, anchor='w')
lblpaksiw.grid(row=5, column=0)
txtpaksiw = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=desertpack, bd=6, insertwidth=4, bg="white", justify='right')
txtpaksiw.grid(row=5, column=1)
 
#--------------------------------------------------------------------------------------
lbldrinkset = Label(f1, font=('aria' , 16, 'bold'), text="Drinks", fg="green", bd=10, anchor='w')
lbldrinkset.grid(row=0, column=2)
txtdrinkset = Entry(f1, font=('ariel' , 16, 'bold'), textvariable=drinkset, bd=6, insertwidth=4, bg="white", justify='right')
txtdrinkset.grid(row=0, column=3)
 
lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="red",bd=10,anchor='w')
lblcost.grid(row=1,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="white" ,justify='right')
txtcost.grid(row=1,column=3)
 
lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="red",bd=10,anchor='w')
lblService_Charge.grid(row=2,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="white" ,justify='right')
txtService_Charge.grid(row=2,column=3)
 
lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="red",bd=10,anchor='w')
lblTax.grid(row=3,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTax.grid(row=3,column=3)
 
lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="red",bd=10,anchor='w')
lblSubtotal.grid(row=4,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="white" ,justify='right')
txtSubtotal.grid(row=4,column=3)
 
lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="red",bd=10,anchor='w')
lblTotal.grid(row=5,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="white" ,justify='right')
txtTotal.grid(row=5,column=3)
 
#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="white")
lblTotal.grid(row=6,columnspan=3)
 
btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="blue",command=Ref)
btnTotal.grid(row=7, column=1)
 
btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="green",command=reset)
btnreset.grid(row=7, column=2)
 
btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="red",command=qexit)
btnexit.grid(row=7, column=3)
 
def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Products", bg="darkblue", fg="white", bd=5)
    lblrestaurant.grid(row=0, column=0)
    lblrestaurant = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=2)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="PRICE",bg="darkblue", fg="white", anchor=W)
    lblrestaurant.grid(row=0, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Starter", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="7", fg="red", anchor=W)
    lblrestaurant.grid(row=1, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Veg combo", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="15", fg="red", anchor=W)
    lblrestaurant.grid(row=2, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Meat combo", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="23", fg="red", anchor=W)
    lblrestaurant.grid(row=3, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Kids combo", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="12", fg="red", anchor=W)
    lblrestaurant.grid(row=4, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Desert", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="8", fg="red", anchor=W)
    lblrestaurant.grid(row=5, column=3)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="Drink", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=0)
    lblrestaurant = Label(roo, font=('aria', 15, 'bold'), text="7", fg="red", anchor=W)
    lblrestaurant.grid(row=6, column=3)
 
    roo.mainloop()
 
btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="white",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="green",command=price)
btnprice.grid(row=7, column=0)
 
root.mainloop()
