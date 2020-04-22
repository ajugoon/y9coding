# Author: A. Jugoon
# Date: April 16th
# Python code to demonstrate the working of 
# choice() and randrange() 
   
# importing "random" for random operations 
import random 
  
# using choice() to generate a random number from a  
# given list of numbers. 
print ("A random number from list is : ",end="") 
print (random.choice([1, 4, 8, 10, 3])) 

print("Generate random integer number within a given range in Python ")
# random.randrange() with only one argument (will not include 10)
print("Random number between 0 and 10 : ", random.randrange(10))

# random.randrange() with two arguments (will not include 40)
print("Random number between 20 and 40 : ", random.randrange(20, 40))

# random.randrange() with three arguments (will look at numbers that increase by 6, 
# but not including 60)
print("Random number between 0 and 60 : ", random.randrange(0, 60, 6))

# Question 1: Can you generate a random 3-digit number?
print("Here is a random 3-digit number: ", random.randrange(100, 1000))
# Question 2: Can you generate a random 4-digit number?
print("Here is a random 4-digit number: ", random.randrange(1000, 10000))
# Question 3: Can you generate a random 4-digit number that is a multiple of 5?
print("Here is a random 4-digit number that is a multiple of 5: ", random.randrange(1000, 10000, 5))
