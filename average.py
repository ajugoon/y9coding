# This is a program that determines the average of three numbers
# Author: Mr. Jugoon
# UCC September 11th, 2019
# Version 1.0
# Still needed: add in a fourth number

number1 = input("What is your first number?") # input received from keyboard by user
print("Your first number is " + number1)

number2 = input("What is your second number?")
print("Your second number is " + number2)

number3 = input("What is your third number?")
print("Your third number is " + number3)

average = (int(number1) + int(number2) + int(number3))/3

print("The average is " + str(average))