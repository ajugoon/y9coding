# Function Example #1

# A simple program that uses the calculates the Area of a circle.
# Area = pi * r * r where pi = 3.14 and "r" is the radius.
import math

print ("")

radius = float(input("Please enter the radius of the circle \n"))

print ("")

area = math.pi * radius * radius

areaRounded = round(area, 4) 

print ("")
print ("The area of the circle is " + str(areaRounded) + " sq. units")



