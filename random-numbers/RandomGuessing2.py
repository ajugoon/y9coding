
# Python code to demonstrate the working of 
# choice() and randrange() 
   
# importing "random" for random operations 
import random 
  

print("A random number between 0 and 10 (inclusive) has been generated")
# random.randrange() with only one argument (will not include 11)

myRandomNum = random.randrange(11)

myNum = int(input("What is your guess? \n"))
print("You have guessed: ", myNum)


if (myNum > myRandomNum):
    print("Your guess was too high!")
    print("The random number was: ", myRandomNum)
elif (myNum < myRandomNum):
    print("Your guess was too low!")
    print("The random number was: ", myRandomNum)
elif (myNum == myRandomNum):
    print("That's it!")
elif (myNum > 10):
    print("This number exceeds the max range")
elif (myNum < 0):
    print("This number is below the min range")
else:
	print ("Invalid number")
 
# This is a way to gracefully exit the program
input("Press ENTER to quit the program")

