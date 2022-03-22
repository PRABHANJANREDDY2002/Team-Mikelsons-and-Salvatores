import tkinter as tk
from tkinter import *
from tkinter import messagebox
import psycopg2
con = psycopg2.connect(
   database="bankmanagementsystem", user='postgres', password='123456', host='127.0.0.1', port= '5432'
)
cur = con.cursor()
cur.execute("SELECT username, pswd from login")
rows = cur.fetchall()
  
 
def submitact():
     
    user = Username.get()
    passw = password.get()
  
    
  
    logintodb(user, passw)
  
 
def logintodb(user, passw):
    c=0
    for row in rows:
        if (row[0] == user and row[1]==passw ):
            print(row)
            c=1
            messagebox.showinfo("Information","Success")
    if(c==0):
            messagebox.showerror("Error","Invalid")
     
    # If password is enetered by the
    # user
    
root = tk.Tk()
root.geometry("300x300")
root.title("DBMS Login Page")
  
 
# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)
 
Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)
  
lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)
 
password = tk.Entry(root, width = 35)
password.place(x = 150, y = 50, width = 100)
 
submitbtn = tk.Button(root, text ="Login",
                      bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)
 
root.mainloop()


 

