from dbcon import *
import tkinter as tk
from tkinter import messagebox
from account import *
from main import *


root = tk.Tk()
root.title("finance holding bank")
root.config(bg='#3F3351')

myAcc = Account()

class withdraw:
    def withdraw_btn():
      global login_frame, withdraw_frame
      global t1_withdraw, t2_withdraw, t3_withdraw, t4_withdraw, t5_withdraw
      t1_withdraw.delete(0, tk.END)
      t2_withdraw.delete(0, tk.END)
      t3_withdraw.delete(0, tk.END)
      t4_withdraw.delete(0, tk.END)
      t5_withdraw.delete(0, tk.END)
      login_frame.pack_forget()
      withdraw_frame.pack()
    def update_withdraw():
        global t2_withdraw, t5_withdraw, myAcc, balance_login_lbl, login_frame, withdraw_frame
        c=myAcc.balance
        if t2_withdraw.get() == myAcc.pin:
            try:
                amount_withdraw = int(t5_withdraw.get())
                if amount_withdraw < myAcc.balance:
                    click = messagebox.askyesno('withdraw', "do you want to withdraw?")
                    if click:
                     myAcc.balance -= amount_withdraw
                     cur.execute(f"UPDATE database SET balance = {myAcc.balance} WHERE Account = {myAcc.accNo}")
                     cur.execute(""" INSERT INTO statements(account,t_type,b_bal,amount,a_bal) VALUES (%s,%s,%s,%s,%s)""", (myAcc.accNo,"withdraw",c,str(amount_withdraw),myAcc.balance))

                     con.commit()
                     balance_login_lbl = tk.Label(login_frame, text=f"balance: {myAcc.balance}", font=('calibri', 27),
                                                 fg='white',
                                                 bg='black').grid(row=2, column=4, columnspan=2)
                     messagebox.showinfo('info', 'amount has been withdraw')
                     withdraw_frame.pack_forget()
                     login_frame.pack()
                    else:
                         return
                else:
                     messagebox.showwarning('warning', 'insufficient amount')
                     return
            except:
                messagebox.showwarning('error', "please reenter amount")
                return
        else:
            messagebox.showwarning('warning', 'invalid pin')
            return

