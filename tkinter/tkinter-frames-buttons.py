
# https://stackoverflow.com/questions/20822553/align-tabs-from-right-to-left-using-ttk-notebook-widget

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My TKinter Hack")
root.minsize(300, 300)
root.geometry("1000x700")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
# style.configure('lefttab.TNotebook', tabposition='ws')

# Create your variables to store data that is typed in by the user 
number1 = tk.StringVar()
number2 = tk.StringVar()

# Helper Functions

def pressBtn1():
    num1 = (number1.get())
    result = int(num1) * 1000
    label2.config(text="Result is %d" % result + "meters")

def pressBtn2():
    num1 = (number1.get())
    result = int(num1) * 100000
    label2.config(text="Result is %d" % result + "centimeters")


planner = ttk.Notebook(root, width=1000, height=650)

# Create the frames of different colours that are 200*200 pixels in dimensions

######################################## Start Frame 1 ###################################

tab1 = tk.Frame(planner, bg='red', width=200, height=200)

# Here we create a label to tell the user of what to do
label1 = tk.Label(tab1, text="Enter your Kilometers")
label1.grid(row=0, column=2)

# Here we create a label to tell the user what the answer is
label2 = tk.Label(tab1, text="Answer is:")
label2.grid(row=1, column=2)

# Here we create a textbox for data entry
# "number1" will store this information that will be used by the "pressBtn1" helper function
entryNum1 = tk.Entry(tab1, textvariable=number1)
entryNum1. grid(row=2, column=2)

# Here we create a button
button1 = tk.Button(tab1, text="Meters", command = pressBtn1)
button1.grid(row=3, column=2)

# Here we create another button
button2 = tk.Button(tab1, text="Centimeters", command = pressBtn2)
button2.grid(row=4, column=2)

######################################## End Frame 1 ###################################

# These frames have not been implemented yet
tab2 = tk.Frame(planner, bg='orange', width=200, height=200)
tab3 = tk.Frame(planner, bg='yellow', width=200, height=200)
tab4 = tk.Frame(planner, bg='green', width=200, height=200)
tab5 = tk.Frame(planner, bg='blue', width=200, height=200)
tab6 = tk.Frame(planner, bg='indigo', width=200, height=200)
tab7 = tk.Frame(planner, bg='violet', width=200, height=200)


# Add the tabs/frames to the notebook object called "planner" 
# Referred to Stack Overflow for assistance

planner.add(tab1, text='Distance')
planner.add(tab2, text='Tempurature')
planner.add(tab3, text='Weight')
planner.add(tab4, text="Wednesday")
planner.add(tab5, text="Thursday")
planner.add(tab6, text="Friday")
planner.add(tab7, text="Saturday")


# Tabs will be added to the "top" of the "frame"
#planner.pack(side=tk.TOP)
planner.grid(row = 0, column = 0)

root.mainloop()
