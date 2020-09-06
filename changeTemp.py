# Function Example

# A simple program that uses the converts a temperature from Fahrenheit to Celsius.

def fahr_to_celsius(celsiusTemp):
    """ returns the temperature in degrees Fahrenheit """
    return (celsiusTemp * 9 / 5) + 32

for temp in (22.6, 25.8, 27.3, 29.8):
    print(temp, " : ", fahr_to_celsius(temp))



