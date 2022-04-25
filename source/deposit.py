from dbcon import *
import tkinter as tk
from tkinter import messagebox
from account import *
from main import *
root = tk.Tk()
root.title("finance holding bank")
root.config(bg='#3F3351')

myAcc = Account()
class deposit:
    def show_btn_deposit():
      global t1_deposit, t2_deposit, t3_deposit, t4_deposit, t5_deposit
      global myAcc
      t1_deposit.delete(0, tk.END)
      t2_deposit.delete(0, tk.END)
      t3_deposit.delete(0, tk.END)
      t4_deposit.delete(0, tk.END)
      t5_deposit.delete(0, tk.END)
      t1_deposit.insert(0, myAcc.accNo)
      t3_deposit.insert(0, myAcc.name)
      t4_deposit.insert(0, myAcc.phone)
      messagebox.showinfo("guideline", "enter pin and Amount")
    def update_deposit():
      global t2_deposit, t5_deposit, myAcc, balance_login_lbl, login_frame, deposit_frame
      if t2_deposit.get() == myAcc.pin:
        try:
            amount_deposit = int(t5_deposit.get())

            click = messagebox.askyesno('withdraw', "do you want to deposit?")
            c=myAcc.balance
            if click:
                myAcc.balance += amount_deposit
                cur.execute(f"UPDATE database SET balance = {myAcc.balance} WHERE Account = {myAcc.accNo}")
                cur.execute(""" INSERT INTO statements(account,t_type,b_bal,amount,a_bal) VALUES (%s,%s,%s,%s,%s)""", (myAcc.accNo,"deposit",c,str(amount_deposit),myAcc.balance))

                con.commit()
                balance_login_lbl = tk.Label(login_frame, text=f"balance: {myAcc.balance}", font=('calibri', 27),
                                                 fg='white',
                                                 bg='black').grid(row=2, column=4, columnspan=2)
                messagebox.showinfo('info', 'amount has been deposit')
                deposit_frame.pack_forget()
                login_frame.pack()
            else:
                return

        except:
            messagebox.showwarning('error', "please reenter amount")
            return
      else:
        messagebox.showwarning('warning', 'invalid pin')
        return




