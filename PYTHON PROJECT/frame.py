from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
conn=sqlite3.connect('ostl1.db')
c=conn.cursor()
global cui


class user_class():
    def __init__(self,fname,lname,uname,mob,pas):
        self.fname=fname
        self.lname=lname
        self.uname=uname
        self.mob=mob
        self.pas=pas

    def insertdb(self):
        c.execute('CREATE TABLE IF  NOT EXISTS cust(cust_fname TEXT,cust_lname TEXT,cust_uname TEXT,cust_mob TEXT,pas TEXT)')
        c.execute("INSERT INTO cust(cust_fname,cust_lname,cust_uname,cust_mob,pas) VALUES(?,?,?,?,?)",
              (self.fname,self.lname,self.uname,self.mob,self.pas))
        
        conn.commit()


class frame1(Frame):
    def __init__(self):
        Frame.__init__(self,master=None)
        
        self.grid()
        self.configure(bg="orange")

        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.master.title('ostl project')
        
        self.lab=Label(self,text="     THE FOOD STUDIO",bg="orange")
        self.lab.config(font=("times new roman",44))
        self.lab.grid(row=0,column=1,sticky=SE)

        self.lab1=Label(self,text="WELCOME",bg="BLUE",fg="white")
        self.lab1.config(font=("times new roman",35))
        self.lab1.grid(row=2,column=1)

        
        self.photo=PhotoImage(file="th.png")
        self.l1=Label(self,image=self.photo,bg="orange")
        self.l1.grid(row=3,column=0)

        self.photo1=PhotoImage(file="img2.png")
        self.l2=Label(self,image=self.photo1)
        self.l2.grid(row=3,column=1)

        self.photo2=PhotoImage(file="img3.png")
        self.l3=Label(self,image=self.photo2)
        self.l3.grid(row=3,column=2,sticky=SW)

        self.photo3=PhotoImage(file="food1.png")
        self.l4=Label(self,image=self.photo3)
        self.l4.grid(row=4,column=0)

        self.photo4=PhotoImage(file="food2.png")
        self.l4=Label(self,image=self.photo4)
        self.l4.grid(row=4,column=1)

        self.photo5=PhotoImage(file="food6.png")
        self.l4=Label(self,image=self.photo5)
        self.l4.grid(row=4,column=2)

        self.but=Button(self,text="NEXT",fg="red",bg="white",command=self.nextw)
        self.but.config(font=("times new roman",24))
        self.but.grid(row=5,column=1)

        self.lab2=Label(self,text="ADDRESS: GROUND FLOOR,BALAJI MOVIEPLEX,SECT-8,KOPARKHAIRANE,NAVI MUMBAI",bg="orange")
        self.lab2.config(font=("times new roman",20))
        self.lab2.grid(row=7,column=0,columnspan=3)
    def nextw(self):
        self.master.destroy()
        root=Tk()
        f11=frame2(root)
        
                
class frame2(Frame):
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x800')
        self.root.configure(bg="white")
        
        self.photo=PhotoImage(file="n2.png")
        self.ph=Label(root,image=self.photo,bg="orange")
        self.ph.place(x=70,y=50)


        self.but1=Button(root,text="SIGN UP",fg="white",bg="green",command=self.nextw1a)
        self.but1.config(font=("times new roman",25))
        self.but1.place(x=590,y=350)


        self.but2=Button(root,text="LOG IN",fg="black",bg="blue",command=self.nextw1b)
        self.but2.config(font=("times new roman",25))
        self.but2.place(x=600,y=480)
        
        self.la3=Label(root,text="    OR     ",fg='black')
        self.la3.config(font=("times new roman",18))
        self.la3.place(x=620,y=435)
        
        self.la1=Label(root,text="NEW USER?")
        self.la1.config(font=("times new roman",18))
        self.la1.place(x=600,y=300)
        
        
        
        self.la2=Label(root,text="ADDRESS: GROUND FLOOR,BALAJI MOVIEPLEX,SECT-8,VASHI,NAVI MUMBAI",bg="orange")
        self.la2.config(font=("times new roman",20))
        self.la2.place(x=170,y=620)

        self.but3=Button(root,text="<-BACK",fg="white",bg="gray",command=self.prev)
        self.but3.config(font=("times new roman",15))
        self.but3.place(x=0,y=0)
        

    def prev(self):
        self.root.destroy()
        a=frame1()
    def nextw1a(self):
        self.root.destroy()
        root1=Tk()
        f11=frame3(root1)
    def nextw1b(self):
        self.root.destroy()
        root2=Tk()
        f11=frame4(root2)
        
class frame3(Frame):
    def __init__(self,root1):
        self.root1=root1
        self.root1.geometry('1350x800')
        self.root1.configure(bg="light green")

        self.la1=Label(root1,text="THE FOOD STUDIO",bg="orange")
        self.la1.config(font=("times new roman",44))
        self.la1.place(x=400,y=10)
        self.la2=Label(root1,text="FIRST NAME",width=12)
        self.la2.config(font=("times new roman",20))
        self.e1=Entry(root1)
        
        self.la2.place(x=500,y=150)
        self.e1.place(x=700,y=150)

        self.la3=Label(root1,text="LAST NAME",width=12)
        self.la3.config(font=("times new roman",20))
        self.e2=Entry(root1)
        self.la3.place(x=500,y=200)
        self.e2.place(x=700,y=200)

        self.la4=Label(root1,text="USER NAME",width=12)
        self.la4.config(font=("times new roman",20))
        self.e3=Entry(root1)
        self.la4.place(x=500,y=250)
        self.e3.place(x=700,y=250)

        self.la5=Label(root1,text="MOBILE",width=12)
        self.la5.config(font=("times new roman",20))
        self.e4=Entry(root1)
        self.la5.place(x=500,y=300)
        self.e4.place(x=700,y=300)

        self.la6=Label(root1,text="PASSWORD",width=12)
        self.la6.config(font=("times new roman",20))
        self.e5=Entry(root1,show='*')
        self.la6.place(x=500,y=350)
        self.e5.place(x=700,y=350)

        self.la7=Label(root1,text="CONFIRM ",width=12)
        self.la7.config(font=("times new roman",20))
        self.e6=Entry(root1,show='*')
        self.la7.place(x=500,y=400)
        self.e6.place(x=700,y=400)

        self.but1=Button(root1,text="SUBMIT",fg="red",bg="white",width=10,command=self.check)
        self.but1.config(font=("times new roman",30))
        self.but1.place(x=400,y=490)

        self.but3=Button(root1,text="BACK",fg="red",bg="white",width=10,command=self.prev)
        self.but3.config(font=("times new roman",30))
        self.but3.place(x=700,y=490)
        
        self.la2=Label(root1,text="ADDRESS: GROUND FLOOR,BALAJI MOVIEPLEX,SECT-8,VASHI,NAVI MUMBAI",bg="orange")
        self.la2.config(font=("times new roman",20))
        self.la2.place(x=150,y=600)
            
    def check(self):
           
        fname=self.e1.get()
        lname=self.e2.get()
        uname=self.e3.get()
        mob=self.e4.get()
        pas=self.e5.get()
        pas1=self.e6.get()

        if(len(fname)==0 or len(lname)==0 or len(uname)==0 or len(mob)==0 or len(pas)==0 or len(pas1)==0):
            messagebox.showerror('Empty Fields!','Please fill all the fields!')
        
            
        elif(pas==pas1):
            c.execute('Select * from cust')
            x=c.fetchall()
            for row in x:
                if row[2]==uname:
                    messagebox.showinfo('Username Taken!','Another user with the same username already exists.')
                    return
                
            my_user=user_class(fname,lname,uname,mob,pas)
            my_user.insertdb()
            messagebox.showinfo('Sign Up Successful!','Your details submitted successfully!!Go back and LogIn')

        else:
            messagebox.showerror('Password Mismatch',"Password and Confirm Password Fields don't match")
            
    def prev(self):
        self.root1.destroy()
        r2=Tk()
        a=frame2(r2)
    
class frame4(Frame):
    def __init__(self,root2):
        self.root2=root2
        self.root2.geometry('1350x800')
        self.root2.configure(bg="green")

        self.la1=Label(root2,text="THE FOOD STUDIO",bg="orange")
        self.la1.config(font=("times new roman",44))
        self.la1.place(x=400,y=100)

        self.la2=Label(root2,text="USER NAME",width=12,bg="orange")
        self.la2.config(font=("times new roman",20))
        self.e1=Entry(root2)
        self.la2.place(x=500,y=250)
        self.e1.place(x=700,y=250)

        self.la3=Label(root2,text="PASSWORD",width=12,bg="orange")
        self.la3.config(font=("times new roman",20))
        self.e2=Entry(root2,show='*')
        self.la3.place(x=500,y=300)
        self.e2.place(x=700,y=300)

        self.but1=Button(root2,text="SIGN IN",fg="white",bg="purple",command=self.check)
        self.but1.config(font=("times new roman",30))
        self.but1.place(x=490,y=450)

        self.but2=Button(root2,text="BACK",fg="white",bg="purple",command=self.prev)
        self.but2.config(font=("times new roman",30))
        self.but2.place(x=690,y=450)


        self.la2=Label(root2,text="ADDRESS: GROUND FLOOR,BALAJI MOVIEPLEX,SECT-8,VASHI,NAVI MUMBAI",bg="orange")
        self.la2.config(font=("times new roman",20))
        self.la2.place(x=190,y=600)

    def prev(self):
        self.root2.destroy()
        r1=Tk()
        a=frame2(r1)
    def check(self):
        flag=0
        uname=self.e1.get()
        pas=self.e2.get()
        if(len(uname)==0 or len(pas)==0):
            messagebox.showerror('Empty Fields','Please Fill all the fields.')
            flag=2
            
        c.execute('Select * from cust')
        x=c.fetchall()
        for row in x:
            if(row[2]==uname and row[4]==pas):
                global my_user
                my_user=user_class(row[0],row[1],row[2],row[3],row[4])
                messagebox.showinfo('Log In Successful!','You can now place your order')
                flag=1
                break
        if(flag==0):
            messagebox.showerror('Log In Error!','No user with the above username and password combination exists')
        if(flag==1):
            self.root2.destroy()
            root5=Tk()
            ff=frame5(root5)
        


class frame5(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")

        self.photo=PhotoImage(file='n2.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=75,y=0)

        self.lab2=Label(master,text="Opening hours: 10 am to 12 pm",bg="orange",fg="green")
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=75,y=205)

        self.lab9=Label(master,text="Happy hours: 1 pm to 8 pm",bg="orange",fg="green")
        self.lab9.config(font=("algerian",18))
        self.lab9.place(x=75,y=248)

        self.lab3=Label(master,text="Phone number:",bg="orange",fg="blue")
        self.lab3.config(font=("algerian",24))
        self.lab3.place(x=75,y=280)

        self.lab4=Label(master,text="022 41576688",bg="orange",fg="black")
        self.lab4.config(font=("algerian",21))
        self.lab4.place(x=75,y=320)

        self.lab5=Label(master,text="Cuisines:",bg="orange",fg="blue")
        self.lab5.config(font=("algerian",24))
        self.lab5.place(x=75,y=352)

        self.lab6=Label(master,text="Chinese, Italian, North Indian, Asian",bg="orange",fg="black")
        self.lab6.config(font=("georgia",21))
        self.lab6.place(x=75,y=390)

        self.lab7=Label(master,text="Continental, South Indian",bg="orange",fg="black")
        self.lab7.config(font=("georgia",21))
        self.lab7.place(x=75,y=427)

        self.lab9=Label(master,text="Get 15% off on your bill during Happy Hours!",bg="orange",fg="dark red")
        self.lab9.config(font=("bookman old style",19))
        self.lab9.place(x=75,y=467)

        self.lab2=Label(master,text="*Cash and Cards Accepted*",bg="orange",fg="red")
        self.lab2.config(font=("bookman old style",18))
        self.lab2.place(x=75,y=498)

        self.button1=Button(master,text="ORDER NOW",bg="green",fg="white",command=self.onlinemenu)
        self.button1.config(font=("bookman old style",23))
        self.button1.place(x=550,y=550)

        self.lab8=Label(master,text="Address:Ground floor, Balaji Movieplex, Sector 8,Kopar khairane , Navi Mumbai",bg="black",fg="white")
        self.lab8.config(font=("algerian",24))
        self.lab8.place(x=10,y=630)

    def onlinemenu(self):
        self.master.destroy()
        root=Tk()
        f6=frame6(root)

class frame6(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Online Ordering Menu",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=400,y=0)

        self.button1=Button(master,text="VIEW CART",bg="green",fg="white")
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1165,y=10)

        self.photo=PhotoImage(file='img2.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=130,y=100)

        self.button2=Button(master,text="STARTERS",bg="white",fg="black",command=self.starters)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=180,y=280)

        self.photo1=PhotoImage(file='snacks.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=530,y=100)

        self.button3=Button(master,text="SNACKS",bg="white",fg="black",command=self.snack)
        self.button3.config(font=("bookman old style",19))
        self.button3.place(x=590,y=280)

        self.photo2=PhotoImage(file='rice.png')
        self.lab4=Label(master,image=self.photo2,bg="orange")
        self.lab4.place(x=920,y=100)

        self.button4=Button(master,text="RICE",bg="white",fg="black",command=self.ricefn)
        self.button4.config(font=("bookman old style",19))
        self.button4.place(x=1000,y=280)

        self.photo3=PhotoImage(file='roti.png')
        self.lab5=Label(master,image=self.photo3,bg="orange")
        self.lab5.place(x=130,y=400)

        self.button5=Button(master,text="BREADS",bg="white",fg="black",command=self.breadsfn)
        self.button5.config(font=("bookman old style",19))
        self.button5.place(x=190,y=580)

        self.photo4=PhotoImage(file='mains.png')
        self.lab6=Label(master,image=self.photo4,bg="orange")
        self.lab6.place(x=530,y=400)

        self.button6=Button(master,text="MAIN COURSE",bg="white",fg="black",command=self.mains)
        self.button6.config(font=("bookman old style",19))
        self.button6.place(x=555,y=580)

        self.photo5=PhotoImage(file='dessert.png')
        self.lab7=Label(master,image=self.photo5,bg="orange")
        self.lab7.place(x=920,y=400)

        self.button7=Button(master,text="DESSERTS",bg="white",fg="black",command=self.dessert)
        self.button7.config(font=("bookman old style",19))
        self.button7.place(x=970,y=580)

        self.button8=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button8.config(font=("bookman old style",19))
        self.button8.place(x=10,y=10)

    def goback(self):
        self.master.destroy()
        r=Tk()
        f=frame5(r)

    def viewc():
        pass

    def starters(self):
        self.master.destroy()
        a1=Tk()
        k=starters1(a1)

    def snack(self):
        self.master.destroy()
        a3=Tk()
        l=snacks(a3)

    def dessert(self):
        self.master.destroy()
        a2=Tk()
        z=desserts(a2)
    def mains(self):
        self.master.destroy()
        a4=Tk()
        f22=maincourse1(a4)
    def ricefn(self):
        self.master.destroy()
        a5=Tk()
        f2=rice(a5)
    def breadsfn(self):
        self.master.destroy()
        a6=Tk()
        f222=breads(a6)

class starters1(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Starters",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1070,y=10)
        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.button3=Button(master,text="NEXT",bg="gray",fg="white",command=self.gonext)
        self.button3.config(font=("bookman old style",19))
        self.button3.place(x=1250,y=10)
        self.lab2=Label(master,text="VEG",fg="blue",bg='orange')
        self.lab2.config(font=("algerian",28))
        self.lab2.place(x=70,y=100)
        self.lab2=Label(master,text="1.Paneer TIKKA                        259.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=185)
        self.lab2=Label(master,text="2.SUBZ SEEKH                             219.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=240)
        self.lab2=Label(master,text="3.TANDOORI MUSHROOM            239.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=295)
        self.lab2=Label(master,text="4.CHEESE CHILLY KEBAB         249.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=350)
        self.lab2=Label(master,text="5.ALOO TIKKA                             199.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=405)
        self.lab2=Label(master,text="6.CHEESE CORN BALLS              279.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=460)
        self.lab2=Label(master,text="7.SPRING ROLLS                          269.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=515)

        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",15))
        self.add1.place(x=700,y=185)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",15))
        self.add2.place(x=700,y=240)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",15))
        self.add3.place(x=700,y=295)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",15))
        self.add4.place(x=700,y=350)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",15))
        self.add5.place(x=700,y=405)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",15))
        self.add6.place(x=700,y=460)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",15))
        self.add7.place(x=700,y=515)

        self.photo=PhotoImage(file='ptikka.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=185)
        self.photo1=PhotoImage(file='sroll.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=400)

        self.add1.bind('<Button-1>',self.item1)
        
        self.add2.bind('<Button-1>',self.item2)
       
        self.add3.bind('<Button-1>',self.item3)
      
        self.add4.bind('<Button-1>',self.item4)
    
        self.add5.bind('<Button-1>',self.item5)
       
        self.add6.bind('<Button-1>',self.item6)
        
        self.add7.bind('<Button-1>',self.item7)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,18))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,19))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,20))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,21))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,22))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,23))
        conn.commit()
        
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,24))
        conn.commit()

        
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)



    def goback(self):
        self.master.destroy()
        a=Tk()
        f=frame6(a)

    def gonext(self):
        self.master.destroy()
        b=Tk()
        k=starters2(b)



class starters2(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Starters",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)        
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1170,y=10)
        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.lab2=Label(master,text="NON-VEG",fg="blue",bg='orange')
        self.lab2.config(font=("algerian",28))
        self.lab2.place(x=70,y=100)
        self.lab2=Label(master,text="8.CHICKEN TIKKA                        289.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=185)
        self.lab2=Label(master,text="9.SEEKH KEBAB                          269.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=240)
        self.lab2=Label(master,text="10.BANJARA KEBAB                    289.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=12,y=295)
        self.lab2=Label(master,text="11.CHICKEN TANDOORI                 350.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=12,y=350)
        self.lab2=Label(master,text="12.FISH TAWA FRY                        429.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=12,y=405)
        self.lab2=Label(master,text="13.CHICKEN MOMOS                       249.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=12,y=460)
        self.lab2=Label(master,text="14.HYDERABADI KEBAB              329.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=12,y=515)

        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",15))
        self.add1.place(x=700,y=185)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",15))
        self.add2.place(x=700,y=240)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",15))
        self.add3.place(x=700,y=295)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",15))
        self.add4.place(x=700,y=350)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",15))
        self.add5.place(x=700,y=405)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",15))
        self.add6.place(x=700,y=460)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",15))
        self.add7.place(x=700,y=515)

        self.photo=PhotoImage(file='ctikka.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=185)
        self.photo1=PhotoImage(file='clolli.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=400)


        self.add1.bind('<Button-1>',self.item1)
        
        self.add2.bind('<Button-1>',self.item2)
       
        self.add3.bind('<Button-1>',self.item3)
      
        self.add4.bind('<Button-1>',self.item4)
    
        self.add5.bind('<Button-1>',self.item5)
       
        self.add6.bind('<Button-1>',self.item6)
        
        self.add7.bind('<Button-1>',self.item7)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,25))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,26))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,27))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,28))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,29))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,30))
        conn.commit()
        
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,31))
        conn.commit()

        
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)



    def goback(self):
        self.master.destroy()
        a=Tk()
        f=starters1(a)

class snacks(Frame):
        
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Snacks",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=550,y=0)        
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1170,y=10)
        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.lab2=Label(master,text="1.French fries                              99.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=130)
        self.lab2=Label(master,text="2.Fish Fingers                               159.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=185)
        self.lab2=Label(master,text="3.Loaded Nachos                         169.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=240)
        self.lab2=Label(master,text="4.Cheesy Tacos                            199.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=295)
        self.lab2=Label(master,text="5.Melted Bruschetta               169.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=350)
        self.lab2=Label(master,text="6.Pizza Mexicano                        429.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=405)
        self.lab2=Label(master,text="7.Margherita Pizza                  349.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=460)
        self.lab2=Label(master,text="8.Mozzarella Sticks                199.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=515)
        self.lab2=Label(master,text="9.Chicken Lasagne                     219.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=570)
        self.lab2=Label(master,text="10.Penne Pesto Pasta                 199.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=12,y=625)

        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",15))
        self.add1.place(x=700,y=130)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",15))
        self.add2.place(x=700,y=185)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",15))
        self.add3.place(x=700,y=240)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",15))
        self.add4.place(x=700,y=295)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",15))
        self.add5.place(x=700,y=350)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",15))
        self.add6.place(x=700,y=405)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",15))
        self.add7.place(x=700,y=460)
        self.add8=Button(master,text="ADD",bg="white",fg="RED")
        self.add8.config(font=("bookman old style",15))
        self.add8.place(x=700,y=515)
        self.add9=Button(master,text="ADD",bg="white",fg="RED")
        self.add9.config(font=("bookman old style",15))
        self.add9.place(x=700,y=570)
        self.add10=Button(master,text="ADD",bg="white",fg="RED")
        self.add10.config(font=("bookman old style",15))
        self.add10.place(x=700,y=625)

        self.photo=PhotoImage(file='snack1.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=130)
        self.photo1=PhotoImage(file='snack2.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=313)
        self.photo2=PhotoImage(file='snack3.png')
        self.lab3=Label(master,image=self.photo2,bg="orange")
        self.lab3.place(x=1000,y=495)




        self.add1.bind('<Button-1>',self.item1)
        
        self.add2.bind('<Button-1>',self.item2)
       
        self.add3.bind('<Button-1>',self.item3)
      
        self.add4.bind('<Button-1>',self.item4)
    
        self.add5.bind('<Button-1>',self.item5)
       
        self.add6.bind('<Button-1>',self.item6)
        
        self.add7.bind('<Button-1>',self.item7)

        self.add8.bind('<Button-1>',self.item8)

        self.add9.bind('<Button-1>',self.item9)
        
        self.add10.bind('<Button-1>',self.item10)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,8))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,9))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,10))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,11))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,12))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,13))
        conn.commit()
        
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,14))
        conn.commit()


        
    def item8(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,15))
        conn.commit()


    def item9(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,16))
        conn.commit()


    def item10(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,17))
        conn.commit()



        
    

        
    

        
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)



    def goback(self):
        self.master.destroy()
        a=Tk()
        f=frame6(a)

   

    
class desserts(Frame):
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,1))
    
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,2))
    
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,3))
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,4))
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,5))
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,6))
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,7))
    
       
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Dessert",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1170,y=10)

        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.lab2=Label(master,text="1.CHOCO LAVA CAKE        189.00 ",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=120)
        self.lab2=Label(master,text="2.CARAMEL CUSTARD       159.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=190)
        self.lab2=Label(master,text="3.CHOCOLATE ROLLS         159.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=260)
        self.lab2=Label(master,text="4.GULAB JAMUN                 99.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=330)
        self.lab2=Label(master,text="5.MALAI KULFI                    129.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=400)
        self.lab2=Label(master,text="6.SIZZLING BROWNIE         189.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=470)
        self.lab2=Label(master,text="7.BROWNIE SUNDAE           199.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=540)
        self.photo=PhotoImage(file='choco.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=150)
        self.photo1=PhotoImage(file='brownie.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=400)

        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",20))
        self.add1.place(x=700,y=120)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",20))
        self.add2.place(x=700,y=190)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",20))
        self.add3.place(x=700,y=260)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",20))
        self.add4.place(x=700,y=330)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",20))
        self.add5.place(x=700,y=400)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",20))
        self.add6.place(x=700,y=470)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",20))
        self.add7.place(x=700,y=540)
        self.add1.bind('<Button-1>',self.item1)
        self.add2.bind('<Button-1>',self.item2)
        self.add3.bind('<Button-1>',self.item3)
        self.add4.bind('<Button-1>',self.item4)
        self.add5.bind('<Button-1>',self.item5)
        self.add6.bind('<Button-1>',self.item6)
        self.add7.bind('<Button-1>',self.item7)
        conn.commit()
    
        
    

    def goback(self):
        self.master.destroy()
        a=Tk()
        f=frame6(a)
        
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)

class maincourse1(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Main Course",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1070,y=10)
        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.button3=Button(master,text="NEXT",bg="gray",fg="white",command=self.gonext)
        self.button3.config(font=("bookman old style",19))
        self.button3.place(x=1250,y=10)
        self.lab2=Label(master,text="VEG",fg="blue",bg='orange')
        self.lab2.config(font=("algerian",28))
        self.lab2.place(x=70,y=100)
        self.lab2=Label(master,text="1.Paneer Pasanda                           295.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=185)
        self.lab2=Label(master,text="2.Paneer Zafrani                            305.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=240)
        self.lab2=Label(master,text="3.Veg Maratha                                 245.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=295)
        self.lab2=Label(master,text="4.Veg Kolhapuri                               275.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=350)
        self.lab2=Label(master,text="5.Paneer Palak                               305.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=405)
        self.lab2=Label(master,text="6.Kofta Angoori                              310.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24)) 
        self.lab2.place(x=30,y=460)
        self.lab2=Label(master,text="7.Mixed Vegetable Makhani      235.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=515)
        self.lab2=Label(master,text="8.Bhindi Amritsari                          240.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=570)
        self.lab2=Label(master,text="9.Aloo Methi                                      215.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=625)
        





        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",15))
        self.add1.place(x=700,y=185)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",15))
        self.add2.place(x=700,y=240)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",15))
        self.add3.place(x=700,y=295)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",15))
        self.add4.place(x=700,y=350)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",15))
        self.add5.place(x=700,y=405)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",15))
        self.add6.place(x=700,y=460)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",15))
        self.add7.place(x=700,y=515)
        self.add8=Button(master,text="ADD",bg="white",fg="RED")
        self.add8.config(font=("bookman old style",15))
        self.add8.place(x=700,y=570)
        self.add9=Button(master,text="ADD",bg="white",fg="RED")
        self.add9.config(font=("bookman old style",15))
        self.add9.place(x=700,y=625)
        


        

        self.photo=PhotoImage(file='kadai1.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=195)
        self.photo1=PhotoImage(file='vegkolhapuri1.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=410)


        self.add1.bind('<Button-1>',self.item1)
        
        self.add2.bind('<Button-1>',self.item2)
       
        self.add3.bind('<Button-1>',self.item3)
      
        self.add4.bind('<Button-1>',self.item4)
    
        self.add5.bind('<Button-1>',self.item5)
       
        self.add6.bind('<Button-1>',self.item6)
        
        self.add7.bind('<Button-1>',self.item7)

        self.add8.bind('<Button-1>',self.item8)

        self.add9.bind('<Button-1>',self.item9)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,39))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,40))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,41))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,42))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,43))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,44))
        conn.commit()
        
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,45))
        conn.commit()


        
    def item8(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,46))
        conn.commit()

        
    def item9(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,47))
        conn.commit()

        
    

        
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)





    def goback(self):
        self.master.destroy()
        a=Tk()
        f=frame6(a)

    def gonext(self):
        self.master.destroy()
        b=Tk()
        s1=maincourse2(b)

    


class maincourse2(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Main Course",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1070,y=10)
        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.button3=Button(master,text="NEXT",bg="gray",fg="white",command=self.gonext)
        self.button3.config(font=("bookman old style",19))
        self.button3.place(x=1250,y=10)
        self.lab2=Label(master,text="DAL",fg="blue",bg='orange')
        self.lab2.config(font=("algerian",28))
        self.lab2.place(x=70,y=100)
        self.lab2=Label(master,text="10.Dal Tadka                                   125.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=185)
        self.lab2=Label(master,text="11.Dal Fry                                         140.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=240)
        self.lab2=Label(master,text="12.Dal Makhani                               255.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=295)
        self.lab2=Label(master,text="13.Dahi Kadhi                                   220.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=350)
        self.lab2=Label(master,text="14.Gujarati Dal                             190.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=405)
        self.lab2=Label(master,text="15.Masoor Dal                                 170.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=460)


        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",15))
        self.add1.place(x=700,y=185)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",15))
        self.add2.place(x=700,y=240)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",15))
        self.add3.place(x=700,y=295)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",15))
        self.add4.place(x=700,y=350)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",15))
        self.add5.place(x=700,y=405)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",15))
        self.add6.place(x=700,y=460)



        



        self.photo=PhotoImage(file='dal.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=250)





        self.add1.bind('<Button-1>',self.item1)
       
        self.add2.bind('<Button-1>',self.item2)
      
        self.add3.bind('<Button-1>',self.item3)
    
        self.add4.bind('<Button-1>',self.item4)
       
        self.add5.bind('<Button-1>',self.item5)
        
        self.add6.bind('<Button-1>',self.item6)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,48))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,49))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,50))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,51))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,52))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,53))
        conn.commit()
        
    
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)


    
        
    
    def goback(self):
        self.master.destroy()
        a=Tk()
        f=maincourse1(a)


    def gonext(self):
        self.master.destroy()
        c=Tk()
        s1=maincourse3(c)

class maincourse3(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Maincourse",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)        
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1170,y=10)
        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.lab2=Label(master,text="NON VEG",fg="blue",bg='orange')
        self.lab2.config(font=("algerian",28))
        self.lab2.place(x=70,y=100)
        self.lab2=Label(master,text="16.Butter Chicken                        305.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=185)
        self.lab2=Label(master,text="17.Chicken Handi                           290.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=240)
        self.lab2=Label(master,text="  18.Chicken Tikka Masala         280.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=12,y=295)
        self.lab2=Label(master,text="19.Murg Patiala                           345.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=350)
        self.lab2=Label(master,text="20.Murg Lahori                              305.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=405)
        self.lab2=Label(master,text="21.Murg Tikka Masala               305.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=460)
        self.lab2=Label(master,text="22.Rawa Fish Curry                     395.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=515)
        self.lab2=Label(master,text="23.Prawns Curry                          410.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=570)
        self.lab2=Label(master,text="24.Pomfret Fry                              400.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=625)

        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",15))
        self.add1.place(x=700,y=185)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",15))
        self.add2.place(x=700,y=240)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",15))
        self.add3.place(x=700,y=295)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",15))
        self.add4.place(x=700,y=350)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",15))
        self.add5.place(x=700,y=405)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",15))
        self.add6.place(x=700,y=460)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",15))
        self.add7.place(x=700,y=515)
        self.add8=Button(master,text="ADD",bg="white",fg="RED")
        self.add8.config(font=("bookman old style",15))
        self.add8.place(x=700,y=570)
        self.add9=Button(master,text="ADD",bg="white",fg="RED")
        self.add9.config(font=("bookman old style",15))
        self.add9.place(x=700,y=625)




        self.photo=PhotoImage(file='chicken.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=130)
        self.photo1=PhotoImage(file='prawns.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=313)
        self.photo2=PhotoImage(file='fish.png')
        self.lab3=Label(master,image=self.photo2,bg="orange")
        self.lab3.place(x=1000,y=495)




        
        self.add1.bind('<Button-1>',self.item1)
        
        self.add2.bind('<Button-1>',self.item2)
       
        self.add3.bind('<Button-1>',self.item3)
      
        self.add4.bind('<Button-1>',self.item4)
    
        self.add5.bind('<Button-1>',self.item5)
       
        self.add6.bind('<Button-1>',self.item6)
        
        self.add7.bind('<Button-1>',self.item7)

        self.add8.bind('<Button-1>',self.item8)

        self.add9.bind('<Button-1>',self.item9)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,54))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,55))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,56))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,57))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,58))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,59))
        conn.commit()
        
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,60))
        conn.commit()


        
    def item8(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,61))
        conn.commit()

        
    def item9(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,62))
        conn.commit()

        
    

        
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)


    

        

    def goback(self):
        self.master.destroy()
        d=Tk()
        f=maincourse2(d)



class rice(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="rice",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1170,y=10)

        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.lab2=Label(master,text="1.PLAIN RICE                                             120.00 ",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=120)
        self.lab2=Label(master,text="2. JEERA RICE                                           150.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=190)
        self.lab2=Label(master,text="3. MOGHLAI VEG BIRYANI                       200.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=260)
        self.lab2=Label(master,text="4. MOGHLAI CHICKEN BIRYANI               300.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=330)
        self.lab2=Label(master,text="5.MOGHLAI FISH BIRYANI                        350.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=400)
        self.lab2=Label(master,text="6.HYDRABADI VEG BIRYANI                   200.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=470)
        self.lab2=Label(master,text="7.HYDRABADI CHICKEN BIRYANI           300.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=540)
        self.photo=PhotoImage(file='rice1.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=150)
        self.photo1=PhotoImage(file='rice2.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=400)

        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",20))
        self.add1.place(x=900,y=120)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",20))
        self.add2.place(x=900,y=190)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",20))
        self.add3.place(x=900,y=260)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",20))
        self.add4.place(x=900,y=330)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",20))
        self.add5.place(x=900,y=400)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",20))
        self.add6.place(x=900,y=470)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",20))
        self.add7.place(x=900,y=540)


        self.add1.bind('<Button-1>',self.item1)
        
        self.add2.bind('<Button-1>',self.item2)
       
        self.add3.bind('<Button-1>',self.item3)
      
        self.add4.bind('<Button-1>',self.item4)
    
        self.add5.bind('<Button-1>',self.item5)
       
        self.add6.bind('<Button-1>',self.item6)
        
        self.add7.bind('<Button-1>',self.item7)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,32))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,33))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,34))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,35))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,36))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,37))
        conn.commit()
        
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,38))
        conn.commit()

        
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)


    def goback(self):
        self.master.destroy()
        a=Tk()
        f=frame6(a)

class breads(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Breads",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=550,y=0)        
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1170,y=10)
        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.lab2=Label(master,text="1.Roti                                           45.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=130)
        self.lab2=Label(master,text="2.Naan                                         55.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=185)
        self.lab2=Label(master,text="3.Kulcha                                     50.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=240)
        self.lab2=Label(master,text="4.Methi Paratha                    70.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=295)
        self.lab2=Label(master,text="5.Methi Roti                              50.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=350)
        self.lab2=Label(master,text="6.Aloo Partaha                     75.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=405)
        self.lab2=Label(master,text="7.Paneer Paratha                 90.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=460)
        self.lab2=Label(master,text="8.Vegetable Kulcha             85.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=515)
        self.lab2=Label(master,text="9.Garlic Naan                          70.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=30,y=570)
        self.lab2=Label(master,text="10.Cheese stuffed naan       115.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",24))
        self.lab2.place(x=12,y=625)

        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",15))
        self.add1.place(x=700,y=130)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",15))
        self.add2.place(x=700,y=185)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",15))
        self.add3.place(x=700,y=240)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",15))
        self.add4.place(x=700,y=295)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",15))
        self.add5.place(x=700,y=350)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",15))
        self.add6.place(x=700,y=405)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",15))
        self.add7.place(x=700,y=460)
        self.add8=Button(master,text="ADD",bg="white",fg="RED")
        self.add8.config(font=("bookman old style",15))
        self.add8.place(x=700,y=515)
        self.add9=Button(master,text="ADD",bg="white",fg="RED")
        self.add9.config(font=("bookman old style",15))
        self.add9.place(x=700,y=570)
        self.add10=Button(master,text="ADD",bg="white",fg="RED")
        self.add10.config(font=("bookman old style",15))
        self.add10.place(x=700,y=625)

        self.photo=PhotoImage(file='Garlicnaan.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=130)
        self.photo1=PhotoImage(file='rotinew.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=313)
        self.photo2=PhotoImage(file='paratha.png')
        self.lab3=Label(master,image=self.photo2,bg="orange")
        self.lab3.place(x=1000,y=495)
        cui='roti'

        self.add1.bind('<Button-1>',self.item1)        
        self.add2.bind('<Button-1>',self.item2)       
        self.add3.bind('<Button-1>',self.item3)     
        self.add4.bind('<Button-1>',self.item4)    
        self.add5.bind('<Button-1>',self.item5)
        self.add6.bind('<Button-1>',self.item6)
        self.add7.bind('<Button-1>',self.item7)
        self.add8.bind('<Button-1>',self.item8)
        self.add9.bind('<Button-1>',self.item9)
        self.add10.bind('<Button-1>',self.item10)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,63))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,64))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,65))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,66))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,67))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,68))
        conn.commit()
        
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,69))
        conn.commit()
    def item8(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,70))
        conn.commit()
    def item9(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,71))
        conn.commit()
    def item10(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,72))
        conn.commit()
    
    
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)



    def goback(self):
        self.master.destroy()
        a=Tk()
        f=frame6(a)


    
class desserts(Frame):
       
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Dessert",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)
        self.button1=Button(master,text="VIEW CART",bg="green",fg="white",command=self.viewc)
        self.button1.config(font=("bookman old style",19))
        self.button1.place(x=1170,y=10)

        self.button2=Button(master,text="BACK",bg="gray",fg="white",command=self.goback)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=10,y=10)
        self.lab2=Label(master,text="1.CHOCO LAVA CAKE        189.00 ",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=120)
        self.lab2=Label(master,text="2.CARAMEL CUSTARD       159.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=190)
        self.lab2=Label(master,text="3.CHOCOLATE ROLLS         159.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=260)
        self.lab2=Label(master,text="4.GULAB JAMUN                 99.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=330)
        self.lab2=Label(master,text="5.MALAI KULFI                    129.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=400)
        self.lab2=Label(master,text="6.SIZZLING BROWNIE         189.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=470)
        self.lab2=Label(master,text="7.BROWNIE SUNDAE           199.00",fg="black",bg='orange')
        self.lab2.config(font=("algerian",30))
        self.lab2.place(x=50,y=540)
        self.photo=PhotoImage(file='choco.png')
        self.lab1=Label(master,image=self.photo,bg="orange")
        self.lab1.place(x=1000,y=150)
        self.photo1=PhotoImage(file='brownie.png')
        self.lab3=Label(master,image=self.photo1,bg="orange")
        self.lab3.place(x=1000,y=400)

        self.add1=Button(master,text="ADD",bg="white",fg="RED")
        self.add1.config(font=("bookman old style",20))
        self.add1.place(x=700,y=120)
        self.add2=Button(master,text="ADD",bg="white",fg="RED")
        self.add2.config(font=("bookman old style",20))
        self.add2.place(x=700,y=190)
        self.add3=Button(master,text="ADD",bg="white",fg="RED")
        self.add3.config(font=("bookman old style",20))
        self.add3.place(x=700,y=260)
        self.add4=Button(master,text="ADD",bg="white",fg="RED")
        self.add4.config(font=("bookman old style",20))
        self.add4.place(x=700,y=330)
        self.add5=Button(master,text="ADD",bg="white",fg="RED")
        self.add5.config(font=("bookman old style",20))
        self.add5.place(x=700,y=400)
        self.add6=Button(master,text="ADD",bg="white",fg="RED")
        self.add6.config(font=("bookman old style",20))
        self.add6.place(x=700,y=470)
        self.add7=Button(master,text="ADD",bg="white",fg="RED")
        self.add7.config(font=("bookman old style",20))
        self.add7.place(x=700,y=540)
        self.add1.bind('<Button-1>',self.item1)
        
        self.add2.bind('<Button-1>',self.item2)
       
        self.add3.bind('<Button-1>',self.item3)
      
        self.add4.bind('<Button-1>',self.item4)
    
        self.add5.bind('<Button-1>',self.item5)
       
        self.add6.bind('<Button-1>',self.item6)
        
        self.add7.bind('<Button-1>',self.item7)
        
        
        
        
       
    def item1(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,1))
        conn.commit()       
      
      
    def item2(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,2))
        conn.commit()
    def item3(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,3))
        conn.commit()
     
    
    def item4(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,4))
        conn.commit()
    
    
    def item5(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,5))
        conn.commit()
     
    
    
    def item6(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,6))
        conn.commit()
        
    
    def item7(self,event):
        c.execute("INSERT INTO purchases(uname,item_id) VALUES(?,?)",(my_user.uname,7))
        conn.commit()
    def viewc(self):
        self.master.destroy()
        b=Tk()
        ob=cart(b)



    def goback(self):
        self.master.destroy()
        a=Tk()
        f=frame6(a)


    


    



class cart(Frame):
    def __init__(self,master):
        Frame.__init__(self,master=None)
        self.master=master
        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.lab2=Label(master,text="Your Cart",bg="orange",fg="green")
        self.lab2.config(font=("algerian",40))
        self.lab2.place(x=500,y=0)

        self.button8=Button(master,text="BACK TO MENU",bg="gray",fg="white",command=self.back)
        self.button8.config(font=("bookman old style",19))
        self.button8.place(x=10,y=10)

        
       
        self.lab3=Label(master,text='ITEM\t\t\t\tQuantity\t\t\tPrice',bg="orange",fg="green")
        self.lab3.config(font=("algerian",20))
        self.lab3.place(x=30,y=150)
        c.execute("select dessertp.name,count(purchases.item_id),sum(dessertp.price) from purchases inner join dessertp on purchases.item_id=dessertp.item_id group by purchases.item_id;")
        x=c.fetchall()
        dist=0
        
        for row in x:
            self.lab3=Label(master,text=str(row[0]),bg="orange",fg="blue")
            self.lab3.config(font=("algerian",20))
            self.lab3.place(x=30,y=200+dist)
            self.lab3=Label(master,text=str(row[1]),bg="orange",fg="blue")
            self.lab3.config(font=("algerian",20))
            self.lab3.place(x=550,y=200+dist)
            self.lab3=Label(master,text=str(row[2]),bg="orange",fg="blue")
            self.lab3.config(font=("algerian",20))
            self.lab3.place(x=925,y=200+dist)
            dist=dist+30

        self.button1=Button(master,text="PLACE ORDER",bg="green",fg="white",command=self.bill)
        self.button1.config(font=("bookman old style",23))
        self.button1.place(x=550,y=600)

        self.button2=Button(master,text="DELETE CART",bg="gray",fg="white",command=self.deleteorder)
        self.button2.config(font=("bookman old style",19))
        self.button2.place(x=980,y=10)
        
        self.button3=Button(master,text="LOG OUT",bg="gray",fg="white",command=self.logout)
        self.button3.config(font=("bookman old style",19))
        self.button3.place(x=1200,y=10)

        

    def bill(self):
        pass

    def back(self):
        self.master.destroy()
        q=Tk()
        bb=frame6(q)

    def deleteorder(self):
        u=my_user.uname
        c.execute("delete from purchases where uname=?",(u,))
        conn.commit()
        self.master.destroy()
        b=Tk()
        f=cart(b)
        
    def logout(self):
        self.master.destroy()
        c=Tk()
        aa=frame4(c)
      

     
    
    
        

        
f11=frame1()
f11.mainloop()
c.close()
conn.close()
