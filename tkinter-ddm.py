# Add your comments here

import tkinter as tk
MyWindow = tk.Tk()
MyWindow.title("Welcome!")
MyWindow.geometry('350x200')

# Create all of the Options that will go into the drop down menu
OPTIONS = [
"Option A",
"Option B",
"Option C",
"Option D",
"Option E",
"Option F"
""
] #etc

# Helper function to give the button functionality
# Helper functions always go above the widgets that are created

def clicked():
    info = "Welcome to " + txt.get()
    lbl.configure(text= info)


# Create the widgets - a Label, Textbox, Button, Dropdown Menu (in that order)

lbl = tk.Label(MyWindow, text = "Hello")
txt = tk.Entry(MyWindow, width = 10)
btn = tk.Button(MyWindow, text = "Click Me", command = clicked)
variable = tk.StringVar(MyWindow) # needed for the dropdown menu (ddm)
variable.set(OPTIONS[0]) # default value
ddm = tk.OptionMenu(MyWindow, variable, *OPTIONS)


# Place all of the widgets into the "imagnary" grid

lbl.grid(column = 0, row = 0)
txt.grid(column = 1, row = 0)
btn.grid(column = 2, row = 0)
ddm.grid(column = 3, row = 1)


MyWindow.mainloop()
