# List Introduction Example
# We can use a String variable to store a collection of items as follows:

# We can include blank spaces in the printout so that it is easier to read
print("")
print("")

# Here the "wizard_list" is a String variable
# It has been used to store a long string of characters
# The String has quotation marks (" ") at the beginning and the end, 
# and makes use of commas to separate items in the set
wizard_list = "spider legs, toe of frog, eye of newt, bat wing, slug butter, snake dandruff"
print("Printing the String variable gives this:")

# Show the items of the String variable "wizard_list"
print(wizard_list)

# Print some blank spaces
print("")
print("")

# Here we have created an actual List item which has square brackets ([ ]) at the beginning and the end
wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
print("Printing the List gives this:")
print(wizard_list)

print("")
print("")

# This allows us to peek at specific sections of the List
# In this exammple, the items at position 1 and 2 will be shown (does NOT go up to 3rd position)
print(wizard_list[1:3])

# This shows the DELETE function
# In this example, the item in the 3rd position will be deleted
# Do a printout of the List to confirm the contents
del wizard_list[3]
print ("performing deletion...")
print (wizard_list)

print("")
print("")

# This shows the APPEND function
# In this example, items will be added to the end of the List
# Do a printout of the List to confirm the contents
wizard_list.append('mandrake')
wizard_list.append('hemlock')
wizard_list.append('swamp gas')
print(wizard_list)

print("")
print("")

# Delete positions 5, 6 and 7
del wizard_list[7]
del wizard_list[6]
del wizard_list[5]
print(wizard_list)

print("")
print("")

