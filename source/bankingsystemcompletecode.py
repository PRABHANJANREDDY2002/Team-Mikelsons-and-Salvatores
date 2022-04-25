import random
from dbcon import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox




root = tk.Tk()
root.resizable(0,0)
root.title("Bank")
root.config(bg='#3F3351')




# In[3]:


def create_btn():
    global create_account_frame
    global home_frame
    global t2, t3, t4
    t2.delete(0, tk.END)
    t3.delete(0, tk.END)
    t4.delete(0, tk.END)
    create_account_frame.pack()
    home_frame.pack_forget()
    myAcc.create_account()

def login_btn():
    myAcc.log_in()


# In[4]:


def cancel_btn():
    global create_account_frame
    global home_frame
    home_frame.pack()
    create_account_frame.pack_forget()


def save_btn():
    global create_account_frame
    global home_frame, t3, t4, t5
    if t3.get() == "" or t4.get() == "" or t5.get() == "":
        messagebox.showwarning("unfilled", "Please fill all entries")
        return

    myAcc.save_acc()
    messagebox.showinfo('saved', "your Account has been created")
    create_account_frame.pack_forget()
    home_frame.pack()


def close_btn():
    global create_account_frame, home_frame, login_frame, closed_frame, transfer_frame, deposit_frame, withdraw_frame
    create_account_frame.pack_forget()
    home_frame.pack_forget()
    login_frame.pack_forget()
    transfer_frame.pack_forget()
    deposit_frame.pack_forget()
    withdraw_frame.pack_forget()
    closed_frame.pack()


# In[5]:


def go_to_transfer_frame():
    global login_frame, transfer_frame
    login_frame.pack_forget()
    transfer_frame.pack()


def transfer_cancel_btn():
    global login_frame, transfer_frame, deposit_frame, withdraw_frame
    transfer_frame.pack_forget()
    deposit_frame.pack_forget()
    withdraw_frame.pack_forget()
    login_frame.pack()


def transfer_btn():
    global login_frame, transfer_frame, balance_login_lbl
    myAcc.transfer_to()
    transfer_frame.pack_forget()
    login_frame.pack()
    balance_login_lbl = tk.Label(login_frame, text=f"balance: {myAcc.balance}", font=('Comic Sans MS', 27), fg='blue',width=30,
                                 bg='black').grid(row=3, column=4, columnspan=4)


# In[6]:


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

def deposit_btn():
    global login_frame, deposit_frame
    global t1_deposit, t2_deposit, t3_deposit, t4_deposit, t5_deposit
    t1_deposit.delete(0, tk.END)
    t2_deposit.delete(0, tk.END)
    t3_deposit.delete(0, tk.END)
    t4_deposit.delete(0, tk.END)
    t5_deposit.delete(0, tk.END)
    login_frame.pack_forget()
    deposit_frame.pack()
    

def show_btn_withdraw():
    global t1_withdraw, t2_withdraw, t3_withdraw, t4_withdraw, t5_withdraw
    global myAcc
    t1_withdraw.delete(0, tk.END)
    t2_withdraw.delete(0, tk.END)
    t3_withdraw.delete(0, tk.END)
    t4_withdraw.delete(0, tk.END)
    t5_withdraw.delete(0, tk.END)
    t1_withdraw.insert(0, myAcc.accNo)
    t3_withdraw.insert(0, myAcc.name)
    t4_withdraw.insert(0, myAcc.phone)
    messagebox.showinfo("guideline", "enter pin and Amount")
    
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


# In[7]:


def delete_btn_login():
    global login_frame, home_frame, myAcc, e1, e2
    click = messagebox.askyesno("delete", "do you want to delete Your account")
    if click:
        cur.execute("DELETE FROM statements WHERE Account like %s", (myAcc.accNo,))
        cur.execute("DELETE FROM database WHERE Account like %s", (myAcc.accNo,))
        con.commit()
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        login_frame.pack_forget()
        home_frame.pack()
    else:
        return


# In[8]:


def update_withdraw():
    global t2_withdraw, t5_withdraw, myAcc, balance_login_lbl, login_frame, withdraw_frame
    if t2_withdraw.get() == myAcc.pin:
        try:
            amount_withdraw = int(t5_withdraw.get())
            if amount_withdraw < myAcc.balance:
                c=myAcc.balance
                click = messagebox.askyesno('withdraw', "do you want to withdraw?")
                if click:
                    myAcc.balance -= amount_withdraw
                    sql = "UPDATE database SET balance = %s WHERE Account = %s"
                    cur.execute(sql,(myAcc.balance,myAcc.accNo))
                    cur.execute(""" INSERT INTO statements(account,t_type,b_bal,amount,a_bal) VALUES (%s,%s,%s,%s,%s)""", (myAcc.accNo,"withdraw",c,str(amount_withdraw),myAcc.balance))

                    con.commit()
                    balance_login_lbl = tk.Label(login_frame, text=f"balance: {myAcc.balance}", font=('Comic Sans MS', 27),width=30,
                                                 fg='blue',
                                                 bg='black').grid(row=3, column=4, columnspan=4)
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
    
def update_deposit():
    global t2_deposit, t5_deposit, myAcc, balance_login_lbl, login_frame, deposit_frame
    if t2_deposit.get() == myAcc.pin:
        try:
            amount_deposit = int(t5_deposit.get())
            c=amount_deposit

            click = messagebox.askyesno('withdraw', "do you want to deposit?")
            if click:
                myAcc.balance += amount_deposit
                sql = "UPDATE database SET balance = %s WHERE Account = %s"
                cur.execute(sql,(myAcc.balance,myAcc.accNo))
                cur.execute(""" INSERT INTO statements(account,t_type,b_bal,amount,a_bal) VALUES (%s,%s,%s,%s,%s)""", (myAcc.accNo,"deposit",c,str(amount_deposit),myAcc.balance))

                con.commit()
                balance_login_lbl = tk.Label(login_frame, text=f"balance: {myAcc.balance}", font=('Comic Sans MS', 27),width=30,
                                                 fg='blue',
                                                 bg='black').grid(row=3, column=4, columnspan=4)
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


# In[9]:
def Transaction_history():
    cur.execute("SELECT * FROM statements  WHERE Account like %s", (myAcc.accNo,))
    rows = cur.fetchall()
    root2 = tk.Tk()  
    tree = ttk.Treeview(root2, column=("c1", "c2", "c3","c4","c5"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Account Number")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Transaction_Type")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Balance_Before_Transaction")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Amount_Used_in_Transaction")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="Balance_After_Transaction")
    tree.pack()    
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row) 



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


# In[10]:


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
            
            

    def transfer_to(self):
        x = t_1.get()
        amount = int(t_3.get())
        pin = t_2.get()
        cur.execute("SELECT Account FROM database")
        sender_acc=cur.fetchall()
        if (x,) in sender_acc and pin == self.pin:
            cur.execute(("SELECT balance FROM database WHERE Account LIKE %s"),(x,))
            sea=cur.fetchone()
            other_account_balance = sea[0]
            if amount < self.balance:
                confirmation = messagebox.askyesno("transfer", "do you want to transfer")
                if not confirmation:
                    return
                else:
                    c=self.balance
                    d=other_account_balance
                    other_account_balance += amount
                    self.balance -= amount
                    cur.execute(("UPDATE database SET balance = %s  WHERE Account = %s "),(other_account_balance,x))
                    cur.execute(("UPDATE database SET balance =%s WHERE Account = %s"), (self.balance,self.accNo))
                    cur.execute(""" INSERT INTO statements(account,t_type,b_bal,amount,a_bal) VALUES (%s,%s,%s,%s,%s)""", (x,"recieved",d,str(amount),other_account_balance))

                    cur.execute(""" INSERT INTO statements(account,t_type,b_bal,amount,a_bal) VALUES (%s,%s,%s,%s,%s)""", (self.accNo,"sent",c,str(amount),self.balance))

                    cur.execute("SELECT * FROM database")
                    
                    db=cur.fetchall()
                    print(db)
                    con.commit()
                    messagebox.showinfo("transferred", "amount transferred successfully!")
            else:
                messagebox.showwarning("error", "Insufficient balance")

        else:
            messagebox.showwarning("error", "Such account does not exist")


# In[11]:


myAcc = Account()
cur.execute("SELECT * FROM database")

print(cur.fetchall())


# In[12]:


# home frame
home_frame = tk.Frame(root)
bank_img = ImageTk.PhotoImage(Image.open("Images/bank_home_page.jpeg"))
img_label = tk.Label(home_frame, image=bank_img).grid(row=0, column=0, columnspan=10)
account_label = tk.Label(home_frame, text="Acc No: ",  font=('Arial', 12), bg = "lightblue").grid(row=1, column=0)
pin_label = tk.Label(home_frame, text="PIN     : ", font=('Arial', 12), bg ="lightblue").grid(row=2, column=0)
e1 = tk.Entry(home_frame,bd=5)
e2 = tk.Entry(home_frame,bd=5,show="*")
btn1_ = tk.Button(home_frame, text="Login", command=login_btn,bg="cyan")
btn2_ = tk.Button(home_frame, text="Create", command=create_btn, bg = "cyan")

e1.grid(row=1, column=1, pady=6, columnspan=6, sticky=tk.W+tk.E, padx=4)
e2.grid(row=2, column=1, pady=6, columnspan=6, sticky=tk.W+tk.E, padx=4)
btn1_.grid(row=3, column=1, pady=5, padx=4, sticky = tk.W+tk.E)

btn2_.grid(row=3, column=2, sticky=tk.W+tk.E, padx=4, pady=5)

home_frame.pack()


# In[13]:


# create account frame
create_account_frame = tk.Frame(root)
lbl1 = tk.Label(create_account_frame, text="Account No")
lbl2 = tk.Label(create_account_frame, text="PIN")
lbl3 = tk.Label(create_account_frame, text="Name")
lbl4 = tk.Label(create_account_frame, text="Amount")
lbl5 = tk.Label(create_account_frame, text="Phone No")

t1 = tk.Entry(create_account_frame,bd=5)
t2 = tk.Entry(create_account_frame,bd=5)
t3 = tk.Entry(create_account_frame,bd=5)
t4 = tk.Entry(create_account_frame,bd=5)
t5 = tk.Entry(create_account_frame,bd=5)

btn1 = tk.Button(create_account_frame, text="Save", command=save_btn)
btn2 = tk.Button(create_account_frame, text="Cancel", command=cancel_btn)
btn3 = tk.Button(create_account_frame, text="Close", command=close_btn)

lbl1.grid(row=0, column=0, padx=60, pady=10)
t1.grid(row=0, column=1, columnspan=2, sticky=tk.W+tk.E, padx=5)
lbl2.grid(row=1, column=0, padx=60, pady=10)
t2.grid(row=1, column=1, columnspan=2, sticky=tk.W+tk.E, padx=5)
lbl3.grid(row=2, column=0, padx=60, pady=10)
t3.grid(row=2, column=1, columnspan=2, sticky=tk.W+tk.E, padx=5)
lbl4.grid(row=3, column=0, padx=60, pady=10)
t4.grid(row=3, column=1, columnspan=2, sticky=tk.W+tk.E, padx=5)
lbl5.grid(row=4, column=0, pady=10)
t5.grid(row=4, column=1, columnspan=2, sticky=tk.W+tk.E, padx=5)


btn1.grid(row=5, column=0, padx=5)
btn2.grid(row=5, column=1, padx=5)
btn3.grid(row=5, column=2, padx=5)


# In[14]:


# login frame
login_frame = tk.Frame(root)

img = ImageTk.PhotoImage(Image.open("Images/login_page.jpeg"))
label_img = tk.Label(login_frame, image=img).grid(row=0, column=0, rowspan=10, columnspan=10)


b1 = tk.Button(login_frame, text="Delete Account", font =
               ('calibri', 20, 'bold'),bg='orange',
            borderwidth ='4', bd=5,activeforeground="orange", activebackground="#B4FE98", width=20, pady=10, command=delete_btn_login)

b2 = tk.Button(login_frame, text="Withdraw", font=
                    ('calibri', 20, 'bold'),bg='orange',
                    borderwidth='4', activeforeground="#678983", activebackground="#B4FE98", width = 20, pady=10, command=withdraw_btn)

b3 = tk.Button(login_frame, text="Deposit", font =
               ('calibri', 20, 'bold'),bg='orange',
            borderwidth = '4', activeforeground="#678983", activebackground="#B4FE98", width = 20, pady=10, command=deposit_btn)

b4 = tk.Button(login_frame, text="Transfer", font =
               ('calibri', 20, 'bold'),bg='orange',
            borderwidth = '4', activeforeground="#678983", activebackground="#B4FE98", width = 20, pady=10, command=go_to_transfer_frame)
b5 = tk.Button(login_frame, text="Close", font =
               ('calibri', 20, 'bold'),bg='orange',
            borderwidth = '4', activeforeground="red", activebackground="pink", width = 20, pady=10,command=close_btn )
b6 = tk.Button(login_frame, text="Transactions", font =
               ('calibri', 20, 'bold'),bg='orange',
            borderwidth = '4', activeforeground="red", activebackground="pink", width = 20, pady=10,command=Transaction_history)

b1.grid(row=0, column=9, pady=10, padx=100)
b2.grid(row=1, column=9, pady=10, padx=100)
b3.grid(row=2, column=9, pady=10, padx=100)
b4.grid(row=3, column=9, pady=10, padx=100)
b5.grid(row=4, column=9, pady=10, padx=100)
b6.grid(row=5, column=9, pady=10, padx=100)


# In[15]:


# transfer frame
transfer_frame = tk.Frame(root)

lb1 = tk.Label(transfer_frame, text="To Account No", font =
               ('calibri', 13, 'bold')).grid(row=0,column=0, pady = 2)
lb2 = tk.Label(transfer_frame, text="PIN", font =
               ('calibri', 13, 'bold')).grid(row=1,column=0,pady = 2)
lb3 = tk.Label(transfer_frame, text="Amount", font =
               ('calibri', 13, 'bold')).grid(row=2,column=0,pady = 2)

t_1 = tk.Entry(transfer_frame,bd=5)
t_2 = tk.Entry(transfer_frame,bd=5,show="*")
t_3 = tk.Entry(transfer_frame,bd=5)

btn_1=tk.Button(transfer_frame, text="Transfer ",bg="light blue", font =
               ('calibri', 11, 'bold'), width = 10, pady=5, borderwidth = '3', activeforeground="black", activebackground="light green",
                command=transfer_btn)
btn_2=tk.Button(transfer_frame, text=" Cancel ",bg="light blue", font =
               ('calibri', 11, 'bold'), width=8, pady=5, borderwidth = '3', activeforeground="red", activebackground="pink",
                command=transfer_cancel_btn)
btn_3=tk.Button(transfer_frame, text=" Close ",bg="light blue", font =
               ('calibri', 11, 'bold'), width=10, pady=5, borderwidth = '3', activeforeground="red", activebackground="#E7EAB5",
                command=close_btn)
t_1.grid(row=0,column=1,pady=10,columnspan=5)
t_2.grid(row=1,column=1,pady=10,columnspan=5)
t_3.grid(row=2,column=1,pady=10,columnspan=5)

btn_1.grid(row=8,column=0,padx=10)
btn_2.grid(row=8,column=1,padx=10)
btn_3.grid(row=8,column=2,padx=10)


# In[16]:


# withdraw frame
withdraw_frame = tk.Frame(root)
lb1_withdraw = tk.Label(withdraw_frame, text="Account No", font =
               ('calibri', 13, 'bold')).grid(row=0,column=0, pady = 2)
lb2_withdraw = tk.Label(withdraw_frame, text="PIN", font =
               ('calibri', 13, 'bold')).grid(row=1,column=0,pady = 2)
lb3_withdraw = tk.Label(withdraw_frame, text="Name", font =
               ('calibri', 13, 'bold')).grid(row=2,column=0,pady = 2)
lb4_withdraw = tk.Label(withdraw_frame, text="Phone No", font =
               ('calibri', 13, 'bold')).grid(row=3,column=0,pady = 2)
lb5_withdraw = tk.Label(withdraw_frame, text="Amount", font =
               ('calibri', 13, 'bold')).grid(row=4,column=0,pady = 2)
t1_withdraw = tk.Entry(withdraw_frame,bd=5)
t2_withdraw = tk.Entry(withdraw_frame,bd=5,show="*")
t3_withdraw = tk.Entry(withdraw_frame,bd=5)
t4_withdraw = tk.Entry(withdraw_frame,bd=5)
t5_withdraw = tk.Entry(withdraw_frame,bd=5)

btn1_withdraw=tk.Button(withdraw_frame, text="Update ", font =
               ('calibri', 11, 'bold'),bg="light blue", width = 10, pady=5, borderwidth='3',bd=5, activeforeground="black",
                        activebackground="light green", command=update_withdraw)
btn2_withdraw=tk.Button(withdraw_frame, text=" Cancel ", font =
               ('calibri', 11, 'bold'),bg="light blue", width=8, pady=5, borderwidth = '3',bd=5, activeforeground="red",
                        activebackground="pink", command=transfer_cancel_btn)
btn3_withdraw=tk.Button(withdraw_frame, text=" Close ", font =
               ('calibri', 11, 'bold'),bg="light blue", width=10, pady=5, borderwidth = '3',bd=5, activeforeground="red",
                        activebackground="#E7EAB5", command=close_btn)
btn4_withdraw=tk.Button(withdraw_frame, text=" Show ", font =
               ('calibri', 11, 'bold'),bg="light blue", width=9, pady=5, borderwidth = '3',bd=5, activeforeground="black",
                        activebackground="#E7EAB5", command=show_btn_withdraw)
t1_withdraw.grid(row=0,column=1,pady=10,columnspan=5)
t2_withdraw.grid(row=1,column=1,pady=10,columnspan=5)
t3_withdraw.grid(row=2,column=1,pady=10,columnspan=5)
t4_withdraw.grid(row=3,column=1,pady=10,columnspan=5)
t5_withdraw.grid(row=4,column=1,pady=10,columnspan=5)

btn1_withdraw.grid(row=8,column=0,padx=10)
btn2_withdraw.grid(row=8,column=1,padx=10)
btn3_withdraw.grid(row=8,column=2,padx=10)
btn4_withdraw.grid(row=0,column=5,padx=2,columnspan=5)


# In[17]:


# deposit frame
deposit_frame = tk.Frame(root)

lb1_deposit = tk.Label(deposit_frame, text="Account No", font =
               ('calibri', 13, 'bold')).grid(row=0,column=0, pady = 2)
lb2_deposit = tk.Label(deposit_frame, text="PIN", font =
               ('calibri', 13, 'bold')).grid(row=1,column=0,pady = 2)
lb3_deposit = tk.Label(deposit_frame, text="Name", font =
               ('calibri', 13, 'bold')).grid(row=2,column=0,pady = 2)
lb4_deposit = tk.Label(deposit_frame, text="Phone No", font =
               ('calibri', 13, 'bold')).grid(row=3,column=0,pady = 2)
lb5_deposit = tk.Label(deposit_frame, text="Amount", font =
               ('calibri', 13, 'bold')).grid(row=4,column=0,pady = 2)
t1_deposit = tk.Entry(deposit_frame,bd=5)
t2_deposit = tk.Entry(deposit_frame,bd=5,show="*")
t3_deposit = tk.Entry(deposit_frame,bd=5)
t4_deposit = tk.Entry(deposit_frame,bd=5)
t5_deposit = tk.Entry(deposit_frame,bd=5)

btn1_deposit=tk.Button(deposit_frame, text="Update ", font =
               ('calibri', 11, 'bold'),bg="light blue", width = 10, pady=5, borderwidth = '3',bd=5, activeforeground="black",
                       activebackground="light green", command=update_deposit)
btn2_deposit = tk.Button(deposit_frame, text=" Cancel ", font =
               ('calibri', 11, 'bold'),bg="light blue", width=8, pady=5, borderwidth = '3',bd=5, activeforeground="red",
                         activebackground="pink", command=transfer_cancel_btn)
btn3_deposit=tk.Button(deposit_frame, text=" Close ", font =
               ('calibri', 11, 'bold'),bg="light blue", width=10, pady=5, borderwidth = '3',bd=5, activeforeground="red",
                       activebackground="#E7EAB5", command=close_btn)
btn4_deposit=tk.Button(deposit_frame, text=" Show ", font =
               ('calibri', 11, 'bold'),bg="light blue", width=9, pady=5, borderwidth='3',bd=5, activeforeground="black",
                       activebackground="#E7EAB5", command=show_btn_deposit)
t1_deposit.grid(row=0, column=1, pady=10, columnspan=5)
t2_deposit.grid(row=1, column=1, pady=10, columnspan=5)
t3_deposit.grid(row=2, column=1, pady=10, columnspan=5)
t4_deposit.grid(row=3, column=1, pady=10, columnspan=5)
t5_deposit.grid(row=4, column=1, pady=10, columnspan=5)

btn1_deposit.grid(row=8, column=0, padx=10)
btn2_deposit.grid(row=8, column=1, padx=10)
btn3_deposit.grid(row=8, column=2, padx=10)
btn4_deposit.grid(row=0, column=5, padx=2, columnspan=5)


# In[18]:


# closed frame
closed_frame = tk.Frame(root)
logo = ImageTk.PhotoImage(Image.open("Images/thankyou.jpeg"))
w = tk.Label(closed_frame,justify=tk.LEFT,
          compound = tk.LEFT,
          padx = 10,

             text="Thankyou \n For Joining Our Bank !!",font =
               ('Algerian', 25, 'bold'),
             image=logo).pack(side="right")

root.mainloop()


# In[19]:


cur.execute("SELECT * FROM database")
print(cur.fetchall())


# In[ ]:




