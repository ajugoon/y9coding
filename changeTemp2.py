# Function Example

# A simple program that uses the converts a temperature from Fahrenheit to Celsius.

########## Function Definition #########

def changeCtoF(celsiusTemp):
    # returns the temperature in degrees Fahrenheit
    return (celsiusTemp * 9 / 5) + 32


########## Main Program ##########

# Using a list to hold the temperature values we want to convert
temps = [22.6, 25.8, 27.3, 29.8]

# Using a FOR loop to examine each temp in the list.
# The 'print' statement will pair up each temperature with
# its corresponding converted value.
# Notice the call to the function that was defined earlier.

for t in temps:

    newT = changeCtoF(t)

    print(t, " : ", newT)



