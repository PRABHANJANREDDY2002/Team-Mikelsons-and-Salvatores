from tkinter import *
from tkinter import messagebox
from functools import partial
from PIL import ImageTk, Image
def main_menu():
    def resize_bg(event):
        global bgg, resized, bg2
        # open image to resize it
        bgg = Image.open("cash-send.jpg")
        # resize the image with width and height of root
        resized = bgg.resize((event.width, event.height),Image.ANTIALIAS)
    
        bg2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=bg2, anchor='nw')
        
    tkWindow = Tk()
    tkWindow.geometry("800x800")  
    tkWindow.title('Banking System')
    
    canvas = Canvas(tkWindow,width=600, height=800)
    canvas.pack(expand=YES, fill=BOTH)
    image = ImageTk.PhotoImage(file="cash-send.jpg")

    canvas.create_image(0, 0, image=image, anchor=NW)
    
    frame1 = Frame(tkWindow , width=600, height=600,bd=5,highlightthickness=2,highlightbackground="black",padx=50,pady=50)
    frame1.pack()
    frame1.place(anchor='center', relx=0.5, rely=0.6)
    usernameLabel = Label(frame1, text="Account Number",pady=15).grid(row=1, column=0)
    username = StringVar()
    usernameEntry = Entry(frame1, textvariable=username).grid(row=1, column=1)

    amountLabel = Label(frame1, text="Enter amount",pady=15).grid(row=2, column=0)
    amount = IntVar()
    amountEntry = Entry(frame1, textvariable=username).grid(row=2, column=1)

    passwordLabel = Label(frame1,text="Password",pady=15).grid(row=3, column=0)
    password = StringVar()
    passwordEntry = Entry(frame1, textvariable=password, show='*').grid(row=3, column=1)  

    loginButton = Button(frame1, text="Send", command=lambda:log_in(username.get(),password.get()),bg = "#88cffa",width=25,height=1).grid(row=4, column=0)
    
    
    tkWindow.bind("<Configure>",resize_bg)
    tkWindow.mainloop()
    
main_menu()
def log_in(user,passw):
    messagebox.showerror("M & S BANK","Invalid Credentials")