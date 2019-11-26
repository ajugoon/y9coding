# A simple translator program, based on example posted online: 
# https://www.codecupboard.com/2017/11/tkinter-set-and-fix-frame-size.html

import tkinter as tk
from tkinter import ttk

MyWindow = tk.Tk()
MyWindow.title("My Translator")

# Defining the window size
MyWindow.geometry("300x200")
# Fixing the window size
MyWindow.resizable(width=False, height=False)
      

# Create your variables to store data that is typed in by the user 
word1 = tk.StringVar()

# Helper Function - to give the button its functionality

def pressBtn1():
    myText1 = str(word1.get())
    # right now it can only do lowercase words!
    if myText1 == "hello":
        result = str("hola")
        label3.config(text=result)
        print (myText1)
    else:
        print ("error " + myText1)
    
# Label
label1 = tk.Label(MyWindow, text = "Enter the Word: ex: 'hello' ")
label2 = tk.Label(MyWindow, text = "The translation is: ")
label3 = tk.Label(MyWindow, text = "????")


# Text Entry
text1 = tk.Entry(MyWindow, textvariable = word1)

# Button
button1 = tk.Button(MyWindow,text='Press',command=pressBtn1)

# Place everything into the grid

label1.grid(row=0,column=0)
text1.grid(row=1,column=0)
button1.grid(row=2,column=0)
label2.grid(row=3,column=0)
label3.grid(row=4,column=0)



MyWindow.mainloop()
