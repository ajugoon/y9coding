# Function Example #1

# A simple program that uses the calculates the Area or Volume of a Shape.

import math

########## Define Your Functions Here ##########

def areaSquare():

    side = float(input("Please enter the length of the side... \n"))

    area = side * side

    areaRounded = round(area, 2) 

    print ("")
    print ("The area of the square is " + str(areaRounded) + " sq. units")

def areaRectangle():

    length = float(input("Please enter the length... \n"))

    width = float(input("Please enter the width... \n"))

    area = length * width

    areaRounded = round(area, 2) 

    print ("")
    print ("The area of the circle is " + str(areaRounded) + " sq. units")

# Area of a Circle = pi * r * r where pi = 3.14... and "r" is the radius.
def areaCircle():

    radius = float(input("Please enter the radius... \n"))

    area = math.pi * radius * radius

    areaRounded = round(area, 4) 

    print ("")
    print ("The area of the circle is " + str(areaRounded) + " sq. units")

########## Main Program Begins Here ##########

print ("1. Calculate the area of a Square")
print ("2. Calculate the area of a Rectangle")
print ("3. Calculate the area of a Circle")
print ("4. Calculate the volume of a Sphere")

choice = int(input("Please choose one of the above options... \n"))

print ("")

if choice == 1:
	areaSquare() # call the function to calculate the area of a square
elif choice == 2:
	areaRectangle() # call the function to calculate the area of a rectangle
elif choice == 3:
	areaCircle() # call the function to calculate the area of a circle
else:
	print("your selection has not been implemented yet")

print ("")
print ("")




