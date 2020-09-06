# Here is a program that shows basic math operations
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Mr. Jugoon
# Upper Canada College

# Tell the user what the program will do...

print ("This program will perform mathematical calculations")

# 'num1' and 'num2' will hold numbers typed in from the keyboard
# and they will be stored as something called a 'float' which
# is another way to say 'decimal'

num1 = float(input("What is the first number? \n"))
num2 = float(input("What is the second number? \n"))

# * is the symbol we use for multiplication
# / is the symbol we use for division
# + is the symbol we use for addition
# - is the symbol we use for subtraction

answer1 = num1 * num2
answer2 = num1 / num2
answer3 = num1 + num2
answer4 = num1 - num2
 

# round the answer to 5 decimal places
# add 'str' so that it can be treated as a sentence

print ("The multiplication will give: " + str(round (answer1, 5)))
print ("The division will give: " + str(round (answer2, 5)))
print ("The addition will give: " + str(round (answer3, 5)))
print ("The subtraction will give: " + str(round (answer4, 5)))
print (" ")

# This is a way to gracefully exit the program
input("Press ENTER to quit the program")