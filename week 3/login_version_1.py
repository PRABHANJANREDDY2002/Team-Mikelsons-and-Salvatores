 
import psycopg2
from tkinter import *

from tkinter import messagebox

from subprocess import call

hostname = 'localhost'
database = 'postgres'
Port_id = 5433
Username = 'postgres'
pwd ='1623'

         



 



def Ok():
     
    conn = psycopg2.connect(
            hostname = 'localhost',
            database = 'Banking_System',
            Username = 'postgres',
            pwd =1623,
            Port_id = 5433)
    Create_Login = '''create table Login (
	               uname varchar(100),
	               password varchar(100) )'''
    cur=conn.cursor(Create_Login)
    conn.commit()
    mycursor=conn.cursor()
    uname = el.get()
    password = e2.get()
    sql = "select from login where uname=%s and password = %s"
    mycursor.execute(sql, [(uname), (password)])
    results = mycursor.fetchall()
    if results:
        messagebox.showinfo("", "Login Success")
        root.destroy()
        call(["python", "Main.py"])
        return True

    else :
        messagebox.showinfo("", "Incorrent Username and Password")
        return False
root = Tk()

root.title("Login")

root.geometry("300x200")

global el

global e2

Label(root, text="UserName").place(x=10, y=10)

Label(root, text="Password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=40)

e2=Entry(root)

e2.place(x=140, y=40)

e2.config(show="*")

Button(root, text="Login", command=Ok,height = 3, width = 13).place(x=10, y=100)

root.mainloop()     
   