from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt

conn = sqlite3.connect('ostl1.db')
c = conn.cursor()
global cui

class user_class():
    def __init__(self, fname, lname, uname, mob, pas):
        self.fname = fname
        self.lname = lname
        self.uname = uname
        self.mob = mob
        self.pas = pas

    def insertdb(self):
        c.execute(
            'CREATE TABLE IF  NOT EXISTS cust(cust_fname TEXT,cust_lname TEXT,cust_uname TEXT,cust_mob TEXT,pas TEXT)')
        c.execute("INSERT INTO cust(cust_fname,cust_lname,cust_uname,cust_mob,pas) VALUES(?,?,?,?,?)",
                  (self.fname, self.lname, self.uname, self.mob, self.pas))

        conn.commit()


class frame1(Frame):
    def __init__(self):
        Frame.__init__(self, master=None)

        self.grid()
        self.configure(bg="orange")

        self.master.geometry('1350x800')
        self.master.configure(bg="orange")
        self.master.title('ostl project')

        self.lab = Label(self, text="     TWITTWER DATA SENTIMENTAL ANALYSIS", bg="orange")
        self.lab.config(font=("times new roman", 44))
        self.lab.grid(row=0, column=1, sticky=SE)

        self.lab1 = Label(self, text="WELCOME", bg="BLUE", fg="white")
        self.lab1.config(font=("times new roman", 35))
        self.lab1.grid(row=2, column=1)

        self.photo1 = PhotoImage(file="Capture.png")
        self.l2 = Label(self, image=self.photo1)
        self.l2.grid(row=4, column=1)


        self.but = Button(self, text="NEXT", fg="red", bg="white", command=self.nextw)
        self.but.config(font=("times new roman", 24))
        self.but.grid(row=6, column=1)


    def nextw(self):
        self.master.destroy()
        root = Tk()
        f11 = frame2(root)


class frame2(Frame):
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x800')
        self.root.configure(bg="white")

        self.photo = PhotoImage(file="sentiment.png")
        self.ph = Label(root, image=self.photo, bg="orange")
        self.ph.place(x=70, y=50)

        self.but1 = Button(root, text="SIGN UP", fg="white", bg="green", command=self.nextw1a)
        self.but1.config(font=("times new roman", 25))
        self.but1.place(x=590, y=350)

        self.but2 = Button(root, text="LOG IN", fg="black", bg="blue", command=self.nextw1b)
        self.but2.config(font=("times new roman", 25))
        self.but2.place(x=600, y=480)

        self.la3 = Label(root, text="    OR     ", fg='black')
        self.la3.config(font=("times new roman", 18))
        self.la3.place(x=620, y=435)

        self.la1 = Label(root, text="NEW USER?")
        self.la1.config(font=("times new roman", 18))
        self.la1.place(x=600, y=300)


        self.but3 = Button(root, text="<-BACK", fg="white", bg="gray", command=self.prev)
        self.but3.config(font=("times new roman", 15))
        self.but3.place(x=0, y=0)

    def prev(self):
        self.root.destroy()
        a = frame1()

    def nextw1a(self):
        self.root.destroy()
        root1 = Tk()
        f11 = frame3(root1)

    def nextw1b(self):
        self.root.destroy()
        root2 = Tk()
        f11 = frame4(root2)


class frame3(Frame):
    def __init__(self, root1):
        self.root1 = root1
        self.root1.geometry('1350x800')
        self.root1.configure(bg="light green")

        self.la1 = Label(root1, text="TWITTER SENTIMENT ANALYSIS SYSTEM", bg="orange")
        self.la1.config(font=("times new roman", 44))
        self.la1.place(x=100, y=10)
        self.la2 = Label(root1, text="FIRST NAME", width=12)
        self.la2.config(font=("times new roman", 20))
        self.e1 = Entry(root1)

        self.la2.place(x=500, y=150)
        self.e1.place(x=700, y=150)

        self.la3 = Label(root1, text="LAST NAME", width=12)
        self.la3.config(font=("times new roman", 20))
        self.e2 = Entry(root1)
        self.la3.place(x=500, y=200)
        self.e2.place(x=700, y=200)

        self.la4 = Label(root1, text="USER NAME", width=12)
        self.la4.config(font=("times new roman", 20))
        self.e3 = Entry(root1)
        self.la4.place(x=500, y=250)
        self.e3.place(x=700, y=250)

        self.la5 = Label(root1, text="MOBILE", width=12)
        self.la5.config(font=("times new roman", 20))
        self.e4 = Entry(root1)
        self.la5.place(x=500, y=300)
        self.e4.place(x=700, y=300)

        self.la6 = Label(root1, text="PASSWORD", width=12)
        self.la6.config(font=("times new roman", 20))
        self.e5 = Entry(root1, show='*')
        self.la6.place(x=500, y=350)
        self.e5.place(x=700, y=350)

        self.la7 = Label(root1, text="CONFIRM ", width=12)
        self.la7.config(font=("times new roman", 20))
        self.e6 = Entry(root1, show='*')
        self.la7.place(x=500, y=400)
        self.e6.place(x=700, y=400)

        self.but1 = Button(root1, text="SUBMIT", fg="red", bg="white", width=10, command=self.check)
        self.but1.config(font=("times new roman", 30))
        self.but1.place(x=400, y=490)

        self.but3 = Button(root1, text="BACK", fg="red", bg="white", width=10, command=self.prev)
        self.but3.config(font=("times new roman", 30))
        self.but3.place(x=700, y=490)


    def check(self):

        fname = self.e1.get()
        lname = self.e2.get()
        uname = self.e3.get()
        mob = self.e4.get()
        pas = self.e5.get()
        pas1 = self.e6.get()

        if (len(fname) == 0 or len(lname) == 0 or len(uname) == 0 or len(mob) == 0 or len(pas) == 0 or len(pas1) == 0):
            messagebox.showerror('Empty Fields!', 'Please fill all the fields!')


        elif (pas == pas1):
            c.execute('Select * from cust')
            x = c.fetchall()
            for row in x:
                if row[2] == uname:
                    messagebox.showinfo('Username Taken!', 'Another user with the same username already exists.')
                    return

            my_user = user_class(fname, lname, uname, mob, pas)
            my_user.insertdb()
            messagebox.showinfo('Sign Up Successful!', 'Your details submitted successfully!!Go back and LogIn')

        else:
            messagebox.showerror('Password Mismatch', "Password and Confirm Password Fields don't match")

    def prev(self):
        self.root1.destroy()
        r2 = Tk()
        a = frame2(r2)


class frame4(Frame):
    def __init__(self, root2):
        self.root2 = root2
        self.root2.geometry('1350x800')
        self.root2.configure(bg="green")

        self.la1 = Label(root2, text="TWITTER SENTIMENT ANALYSIS SYSTEM", bg="orange")
        self.la1.config(font=("times new roman", 44))
        self.la1.place(x=100, y=100)

        self.la2 = Label(root2, text="USER NAME", width=12, bg="orange")
        self.la2.config(font=("times new roman", 20))
        self.e1 = Entry(root2)
        self.la2.place(x=500, y=250)
        self.e1.place(x=700, y=250)

        self.la3 = Label(root2, text="PASSWORD", width=12, bg="orange")
        self.la3.config(font=("times new roman", 20))
        self.e2 = Entry(root2, show='*')
        self.la3.place(x=500, y=300)
        self.e2.place(x=700, y=300)

        self.but1 = Button(root2, text="SIGN IN", fg="white", bg="purple", command=self.check)
        self.but1.config(font=("times new roman", 30))
        self.but1.place(x=490, y=450)

        self.but2 = Button(root2, text="BACK", fg="white", bg="purple", command=self.prev)
        self.but2.config(font=("times new roman", 30))
        self.but2.place(x=690, y=450)


    def prev(self):
        self.root2.destroy()
        r1 = Tk()
        a = frame2(r1)

    def check(self):
        flag = 0
        uname = self.e1.get()
        pas = self.e2.get()
        if (len(uname) == 0 or len(pas) == 0):
            messagebox.showerror('Empty Fields', 'Please Fill all the fields.')
            flag = 2

        c.execute('Select * from cust')
        x = c.fetchall()
        for row in x:
            if (row[2] == uname and row[4] == pas):
                global my_user
                my_user = user_class(row[0], row[1], row[2], row[3], row[4])
                messagebox.showinfo('Log In Successful!')
                flag = 1
                break
        if (flag == 0):
            messagebox.showerror('Log In Error!', 'No user with the above username and password combination exists')
        if (flag == 1):
            self.root2.destroy()
            root5 = Tk()
            ff = frame5(root5)


class frame5(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.master = master
        self.master.geometry('1350x800')
        self.master.configure(bg="purple")
        self.master.title('ML project')
        self.lab = Label(master, text="      TWITTER DATA SENTIMENT ANALYSIS", bg="orange")
        self.lab.config(font=("times new roman", 44))
        self.lab.grid(row=1, column=1)
        self.photo = PhotoImage(file="capture1.png")
        self.ph = Label(master, image=self.photo)
        self.ph.place(x=100, y=350)

        self.la3 = Label(master, text="Enter Keyword/Tag to search about:", width=50)
        self.la3.config(font=("times new roman", 20))
        self.e2 = Entry(master)
        self.la3.place(x=50, y=120)
        self.e2.place(x=850, y=120)

        self.la4 = Label(master, text="Enter how many tweets to search: ", width=50)
        self.la4.config(font=("times new roman", 20))
        self.e3 = Entry(master)
        self.la4.place(x=50, y=190)
        self.e3.place(x=850, y=190)

        self.but = Button(master, text="Get the Result", fg="red", bg="white", command="DownloadData()")
        self.but.config(font=("times new roman", 24))
        self.but.place(x=50, y=250)


        searchTerm=self.e2.get()
        NoOfTerms=self.e3.get()
        self.tweets = []
        self.tweetText = []

    def DownloadData(self, searchTerm, NoOfTerms):
        consumerKey = 'RhQ1DdqGBGd37GJ342yk3hg35'
        consumerSecret = 'Mdg4L6KfoghEwBDIlpt7XEsQBYKmFcAmFcANdt8Tex8gESHVYV'
        accessToken = '3225213469-M5emugNRZ35jnyqsq7Mw7PEK5eUb9sxnxNdcYvW'
        accessTokenSecret = 'ij81GWhw5lscACQ51PEd6dDW0peNALmPzAlYqBOZ0xTux'
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth)

        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang="en").items(NoOfTerms)

        # Open/create a file to append data to
        csvFile = open('result.csv', 'a')

        # Use csv writer
        csvWriter = csv.writer(csvFile)

        # creating some variables to store info
        polarity = 0
        positive = 0
        wpositive = 0
        spositive = 0
        negative = 0
        wnegative = 0
        snegative = 0
        neutral = 0

        # iterating through tweets fetched
        for tweet in self.tweets:
            # Append to temp so that we can store in csv later. I use encode UTF-8
            self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))
            # print (tweet.text.translate(non_bmp_map))    #print tweet's text
            analysis = TextBlob(tweet.text)
            # print(analysis.sentiment)  # print tweet's polarity
            polarity += analysis.sentiment.polarity  # adding up polarities to find the average later

            if (analysis.sentiment.polarity == 0):  # adding reaction of how people are reacting to find average later
                neutral += 1
            elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
                wpositive += 1
            elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
                positive += 1
            elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
                spositive += 1
            elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
                wnegative += 1
            elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
                negative += 1
            elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
                snegative += 1

        csvWriter.writerow(self.tweetText)
        csvFile.close()

        # finding average of how people are reacting
        positive = self.percentage(positive, NoOfTerms)
        wpositive = self.percentage(wpositive, NoOfTerms)
        spositive = self.percentage(spositive, NoOfTerms)
        negative = self.percentage(negative, NoOfTerms)
        wnegative = self.percentage(wnegative, NoOfTerms)
        snegative = self.percentage(snegative, NoOfTerms)
        neutral = self.percentage(neutral, NoOfTerms)

        # finding average reaction
        polarity = polarity / NoOfTerms

        # printing out data
        print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + " tweets.")
        print()
        print("General Report: ")

        if (polarity == 0):
            print("Neutral")
        elif (polarity > 0 and polarity <= 0.3):
            print("Weakly Positive")
        elif (polarity > 0.3 and polarity <= 0.6):
            print("Positive")
        elif (polarity > 0.6 and polarity <= 1):
            print("Strongly Positive")
        elif (polarity > -0.3 and polarity <= 0):
            print("Weakly Negative")
        elif (polarity > -0.6 and polarity <= -0.3):
            print("Negative")
        elif (polarity > -1 and polarity <= -0.6):
            print("Strongly Negative")

        print()
        print("Detailed Report: ")
        print(str(positive) + "% people thought it was positive")
        print(str(wpositive) + "% people thought it was weakly positive")
        print(str(spositive) + "% people thought it was strongly positive")
        print(str(negative) + "% people thought it was negative")
        print(str(wnegative) + "% people thought it was weakly negative")
        print(str(snegative) + "% people thought it was strongly negative")
        print(str(neutral) + "% people thought it was neutral")



f11 = frame1()
f11.mainloop()
c.close()
conn.close()
