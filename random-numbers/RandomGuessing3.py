# Y9 Design Coding - Mr. Jugoon
# In this example we are guessing a randomly generated number
# This is based on the text-based example seen earlier
# Now there is a basic GUI that has been added to it
# Special Programming Note: Use four spaces instead of tab


from tkinter import *
from random import random
from random import randrange

def CheckAnswer():
    

    info1 = ""
    info2 = ""
    myNum = myData.get() # this get the "int" value associated with IntVar called "myData"
    print (myNum)
    print (myRandomNum)
    print (myData)

    if (myNum > myRandomNum):
        info1 = "Your guess was too high!"
        info2 = "The random number was: " + str(myRandomNum)

    elif (myNum < myRandomNum):
        info1 = "Your guess was too low!"
        info2 = "The random number was: " + str(myRandomNum)
        
    elif (myNum == myRandomNum):
        info1 = "Your guess was an exact match!"
        info2 = "How could you possibly know that the number was " + str(myRandomNum) + " ?"

    elif (myNum > 10):
        info1 = "Your guess was way too high!"
        info2 = "Guess was out of range..."
    elif (myNum < 0):
        info1 = "Your guess was way too low!"
        info2 = "Guess was out of range..."
    else:
        info1 = "Invalid"
        info2 = ""

    lbl1.configure(text = info1)
    lbl2.configure(text = info2)

##############################################################################
myRandomNum = randrange(11)

# Create all of the widgets needed: labels, textboxes, buttons, etc.
MyWindow = Tk()
MyWindow.title("Let's play the Guessing Game!")
MyWindow.geometry('600x200')

lbl = Label(MyWindow, text = "Guess a number between 0 and 10 inclusive")
lbl1 = Label(MyWindow, text = "")
lbl2 = Label(MyWindow, text = "")

myData = IntVar()
myChoice = Entry(MyWindow, width = 10, textvariable = myData)
btn = Button(MyWindow, text = "Check", command = CheckAnswer)


# Postion all of the widgets in the window that was created


lbl.grid(column = 0, row = 0)
myChoice.grid(column = 0, row = 1)
btn.grid(column = 1, row = 1)
lbl1.grid(column = 0, row = 2)
lbl2.grid(column = 0, row = 3)


MyWindow.mainloop()

##############################################################################
