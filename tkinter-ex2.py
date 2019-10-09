from tkinter import *
MyWindow = Tk()
MyWindow.title("Welcome to UCC!")
MyWindow.geometry('350x200')
lbl = Label(MyWindow, text="Hello")
lbl.grid(column=0, row=0)
btn = Button(MyWindow, text="Click Me")
btn.grid(column=1, row=0)
MyWindow.mainloop()
