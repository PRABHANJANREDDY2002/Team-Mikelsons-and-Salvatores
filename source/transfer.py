from main import *
from dbcon import *
import tkinter as tk
from tkinter import messagebox
from account import *
cur = con.cursor()
root = tk.Tk()
root.resizable(0,0)
root.title("Bank")
root.config(bg='#3F3351')
myAcc = Account()
class transfer:
    t_1 = tk.Entry(transfer_frame,bd=5)
    t_2 = tk.Entry(transfer_frame,bd=5,show="*")
    t_3 = tk.Entry(transfer_frame,bd=5)
    def transfer_to(myAcc):
        x = t_1.get()
        amount = int(t_3.get())
        pin = t_2.get()
        cur.execute("SELECT Account FROM database")
        sender_acc=cur.fetchall()
        if (x,) in sender_acc and pin == myAcc.pin:
            cur.execute(("SELECT balance FROM database WHERE Account LIKE %s"),(x,))
            sea=cur.fetchone()
            other_account_balance = sea[0]
            if amount < myAcc.balance:
                confirmation = messagebox.askyesno("transfer", "do you want to transfer")
                if not confirmation:
                    return
                else:
                    c=myAcc.balance
                    d=other_account_balance
                    other_account_balance += amount
                    myAcc.balance -= amount
                    cur.execute(("UPDATE database SET balance = %s  WHERE Account = %s "),(other_account_balance,x))
                    cur.execute(("UPDATE database SET balance =%s WHERE Account = %s"), (myAcc.balance,myAcc.accNo))
                    cur.execute(""" INSERT INTO statements(account,t_type,b_bal,amount,a_bal) VALUES (%s,%s,%s,%s,%s)""", (x,"recieved",d,str(amount),other_account_balance))

                    cur.execute(""" INSERT INTO statements(account,t_type,b_bal,amount,a_bal) VALUES (%s,%s,%s,%s,%s)""", (myAcc.accNo,"sent",c,str(amount),myAcc.balance))

                    cur.execute("SELECT * FROM database")
                    
                    db=cur.fetchall()
                    print(db)
                    con.commit()
                    messagebox.showinfo("transferred", "amount transferred successfully!")
            else:
                messagebox.showwarning("error", "Insufficient balance")

        else:
            messagebox.showwarning("error", "Such account does not exist")
