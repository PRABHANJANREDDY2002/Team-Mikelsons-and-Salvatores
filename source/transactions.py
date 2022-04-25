from tkinter import ttk
from account import *

import tkinter as tk

from dbcon import *

myAcc = Account()

def Transaction_history():

    cur.execute("SELECT * FROM statements  WHERE Account like %s", (myAcc.accNo,))

    rows = cur.fetchall()    

    for row in rows:

        print(row) 

        tree.insert("", tk.END, values=row)        




root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5"), show='headings')

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

button1 = tk.Button(text="Display data", command=Transaction_history)

button1.pack(pady=10)

root.mainloop()