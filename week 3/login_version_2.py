import tkinter as tk
from tkinter import *
from tkinter import messagebox
import psycopg2

from login import Acount_Number
con = psycopg2.connect(

             hostname = 'localhost',
            database = 'Banking_System',
            Acount_Numbername = 'postgres',
            pwd =1623,
            Port_id = 5433
)
cur = con.cursor()
cur.execute("SELECT Acount_Number , password from login")
rows = cur.fetchall()
  
 
def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
  
    print(f"The name entered by you is {Acount_Number} {passw}")
  
    logintodb(Acount_Number, passw)
  

    return
def logintodb(Acount_Number, passw):
    c=0
    for row in rows:
        if (row[0] == Acount_Number and row[1]==passw ):
            print(row)
            c=1
            messagebox.showinfo("Information","success")
    if(c==0):
            messagebox.showerror("Error","Error")
     
    # If password is enetered by the
    # Acount_Number
    
root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")
  
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Acount_Number -", )
lblfrstrow.place(x = 50, y = 20)
 
Acount_Number = tk.Entry(root, width = 35)
Acount_Number.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
 
submitbtn = tk.Button(root, text ="Login",
                      bg ='blue', command = validateLogin)
submitbtn.place(x = 150, y = 135, width = 55)
 
root.mainloop()