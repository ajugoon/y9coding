# Here is a program to show how to use "if - elif - else"
# when they are "nested" of "one inside of the other"
#
# 	> means "greater than..."
# 	>= means "greater than or equal to..."
# 	< means "less than..."
# 	<= means "less than or equal to..."
#
# You can use "and" to join conditions together
# Author: Mr. Jugoon
# Upper Canada College
#
# Put down some options for the user to choose from...

print("1. Happy")
print(" ")
print("Choose one of the options above")

mood = int(input("What is your current mood? \n"))

scale = int(input("On a scale from 1 to 10 how do you feel?\n"))

if mood == 1:
  if (scale >= 0 and scale < 5):
      print("Keep having a good day!")
  elif (scale >= 5 and scale < 8):
      print("Well done!")
  elif (scale >= 8 and scale <= 10):
      print("That's beyond awesome!")
  else:
      print ("That's not a valid option!")
elif mood == 2:
    print ("Can I cheer you up?")
elif mood == 3:
    print ("I am very happy for you!")
else:
    print ("This is not a valid choice")
    print ("Hope you have a great day anyway!")


# This is a way to gracefully exit the program
input("Press ENTER to quit the program...")
