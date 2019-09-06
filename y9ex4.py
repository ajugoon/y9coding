# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Put down some options for the user to choose from...

print("1. Happy")
print("2. Sad")
print("3. Excited")
print(" ")
print("Choose one of the options above")

mood = int(input("What is your current mood? \n"))

if mood == 1:
    print("That's awesome!")
elif mood == 2:
    print ("Can I cheer you up?")
elif mood == 3:
    print ("I am very happy for you!")
else:
    print ("This is not a valid choice")
    print ("Hope you have a great day anyway!")


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")
