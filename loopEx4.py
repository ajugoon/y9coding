# Loop Example #4

# Suppose you have been asked to write a simple program that a ticket attendant 
# can use at a movie theatre to determine the price a customer pays. 
# Due to COVID guidelines, you are only allowed to have 10 customers in the theatre 
# at a time. Assuming that you have 10 customers waiting in line, write a program 
# charges the following prices (ignore the tax for now):

# Extension: You can also calculate the final price with 13% tax included

# Prices are as follows:
# ages 3 - 13 (child) $8.99
# ages 14 - 64 (general) $12.50
# ages 65+ (senior) $9.99


print ("Welcome to the Movies!")
print ("Please enter the ages of the customers")

for customer in range (0, 10, 1):
    age = int(input("Enter the customer age..."))

    if (age >= 3 and age <= 13):
        print("This is a Child and will pay $8.99") 

    elif (age >= 14 and age <= 64):
        print("This is a General Admission and will pay $12.50")

    elif age >= 65:
        print("This is a Senior and will pay $9.99") 

    else:
        print("This person goes for free!") 

print ("Thank You!")



