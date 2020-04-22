# This is the same game as before but now there is a button
# that generates another random number so that you can play again.

# Special notes:
# Use four spaces instead of tab
# Only import modules you need

from tkinter import *
from random import random
from random import randrange

def CheckAnswer():

    # A random number is only needed immediately prior to us getting the user input
    myRandomNum = randrange(11)
    print ("The random number is :" + str(myRandomNum))
    info1 = ""
    info2 = ""

    # Here we get the input from the user
    myNum = myData.get() # this get the "int" value associated with IntVar called "myData"
    
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

def PlayAgain():

    info1 = "New Game"
    info2 = "Let's Go!"
    lbl1.configure(text = info1)
    lbl2.configure(text = info2)

##############################################################################


# Create all of the widgets needed: labels, textboxes, buttons, etc.
MyWindow = Tk()
MyWindow.title("Let's Guess the Number!")
MyWindow.geometry('600x200')

lbl = Label(MyWindow, text = "Guess a number between 0 and 10 inclusive")
lbl1 = Label(MyWindow, text = "")
lbl2 = Label(MyWindow, text = "")

myData = IntVar()
myChoice = Entry(MyWindow, width = 10, textvariable = myData)
btnCheck = Button(MyWindow, text = "Check My Guess", command = CheckAnswer)
btnPlayAgain = Button(MyWindow, text = "Play Again", command = PlayAgain)

# Postion all of the widgets in the window that was created

lbl.grid(column = 0, row = 0)
myChoice.grid(column = 0, row = 1)
btnCheck.grid(column = 1, row = 1)
btnPlayAgain.grid(column = 2, row = 1)
lbl1.grid(column = 0, row = 2)
lbl2.grid(column = 0, row = 3)


MyWindow.mainloop()

##############################################################################
