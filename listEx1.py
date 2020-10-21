# List Introduction Example
# We can use a String variable to store a collection of items as follows:



# Here we have created an actual List item which has square brackets ([ ]) at the beginning and the end
city_list = ['Saskatoon', 'Toronto', 'Edmonton', 'Halifax', 'Montreal', 'Fredricton']

print("Printing the List gives this:")
print(city_list)

print("")
print("")

# This allows us to peek at specific sections of the List
# In this example, the items at position 1 and 2 will be shown (does NOT go up to 3rd position)
print(city_list[1:3])

# This shows the DELETE function
# In this example, the item in the 3rd position will be deleted
# Do a printout of the List to confirm the contents
del city_list[3]
print ("performing deletion...")
print (city_list)

print("")
print("")

# This shows the APPEND function
# In this example, items will be added to the end of the List
# Do a printout of the List to confirm the contents
city_list.append("St. John's")
city_list.append("Charlottetown")
city_list.append("Yellowknife")
print(city_list)

print("")
print("")

# Delete positions 5, 6 and 7
del city_list[7]
del city_list[6]
del city_list[5]
print(city_list)

print("")
print("")

