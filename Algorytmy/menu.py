from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("300x300")


def helloCallBack():
    messagebox.showinfo("Say Hello", "Hello World")


def sel():
    messagebox.showinfo("You select " + str(var.get()), "xxx")

def custom():
    L1 = Label(top, text="User Name")
    L1.pack(side = LEFT)
    E1 = Entry(top, bd =5)

    E1.pack(side = RIGHT)

# B = Button(top, text ="Hello", command = helloCallBack)
# circle_button = Button(top, text="Circle")
# B.grid(row=0, column=0)
# circle_button.grid(row=0, column=1)

var = IntVar()
R1 = Radiobutton(top, text="Circle", variable=var, value=1,
                  command=sel)
R2 = Radiobutton(top, text="Custom function", variable=var, value=2,
                 command=custom)

R1.pack( anchor = W )
R2.pack( anchor = W)

top.mainloop()
