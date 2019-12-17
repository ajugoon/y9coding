from tkinter import *
MyWindow = Tk()
MyWindow.title("Welcome to UCC!")
MyWindow.geometry('350x200')
lbl = Label(MyWindow, text="Hello")
lbl.grid(column=0, row=0)
txt = Entry(MyWindow,width=10)
txt.grid(column=1, row=0)
def clicked():
    info = "Welcome to " + txt.get()
    lbl.configure(text= info)
btn = Button(MyWindow, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
MyWindow.mainloop()
