import random
import tkinter as tk
from dbcon import *
from tkinter import messagebox


def checksum(x):
    addition, digit, count = 0, 0, 1
    for i in x:
        if count % 2 != 0:
            if int(i) * 2 > 9:
                addition += int(i) * 2 - 9
            else:
                addition += int(i) * 2
        else:
            addition += int(i)

    for i in range(10):
        if (addition + i) % 10 == 0:
            digit = i
            break
    return digit

class Account:
    def __init__(self):
        self.accNo = ""
        self.pin = ""
        self.name = ""
        self.balance = 0
        self.phone = ""
    

    def create_account(self):
        cur.execute('SELECT Account FROM database')
        accounts = cur.fetchall()
        print(accounts)
        global t1, t2
        while True:
            x = '4000' + str(random.randrange(0, 9999)).zfill(4)
            last_digit = checksum(x)

            x += str(last_digit)

            pin = str(random.randrange(9999)).zfill(4)

            if (x,) not in accounts:
                self.accNo = x
                self.pin = pin
                break

        t1.insert(0, x)
        t2.insert(0, pin)
    
    def save_acc(self):
        global t3, t4, t5
        cur.execute('SELECT Account FROM database')
        accounts = cur.fetchall()
        name = t3.get()  # this will be changed to display the it on gui
        phone = t5.get()  # this will be changed to display the it on gui
        balance = int(t4.get())
        self.name, self.phone, self.balance = name, phone, balance
        postgres_insert_query = """ INSERT INTO database (id, Account, pin, name, balance, phone) VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (len(accounts) + 1, self.accNo, self.pin, self.name, self.balance, self.phone)
        cur.execute(postgres_insert_query,record_to_insert)
        con.commit()
    def log_in(self):
        global e1, e2, home_frame, login_frame
        cur.execute("SELECT Account, pin FROM database")
        all_accounts = cur.fetchall()
        logged_in = False
        acc = e1.get()
        password = e2.get()

        for x, y in all_accounts:
            if acc == x and password == y:
                home_frame.pack_forget()
                login_frame.pack()
                cur.execute("SELECT * from database WHERE  ACCOUNT LIKE %s ", (acc,))
                card_detail = cur.fetchall()
                print(card_detail,acc)
                id, self.accNo, self.pin, self.name, self.balance, self.phone = card_detail[0]
                logged_in = True
                break
        else:
            messagebox.showwarning(title="Error", message="Account No or pin is invalid")
            return

        if logged_in:
            global name_login_lbl, phone_login_lbl, balance_login_lbl,accountno_login_lbl
            
            frame = login_frame

            name_login_lbl = tk.Label(frame, text=f"Name: {self.name}", font=('Comic Sans MS', 27), fg='orange',width=30,
                                      bg='black').grid(row=0, column=4, columnspan=4)

            phone_login_lbl = tk.Label(frame, text=f"mobile No: {self.phone}", font=('Comic Sans MS', 27), fg='white',width=30,
                                       bg='black').grid(row=1, column=4, columnspan=4)
            
            accountno_login_lbl=tk.Label(frame, text=f"Acc NO: {self.accNo}", font=('Comic Sans MS', 27), fg='light green',width=30,
                                       bg='black').grid(row=2, column=4, columnspan=4)

            balance_login_lbl = tk.Label(frame, text=f"balance: {self.balance}", font=("Comic Sans MS", 27), fg='blue',width=30,
                                         bg='black').grid(row=3, column=4, columnspan=4)
            
            