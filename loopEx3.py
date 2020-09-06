# Loop Example #3
# For Loop performs a task a finite number of times and then stops.

provinces_list = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Yukon']

# We can use the built-in capability of a List to be able to print its entire contents
print(provinces_list)
print("")
print("")

# We can use a Loop to have more control
# This loop prints all the provinces
# 13 provinces means they are numbered positions 0 to 12
# However, the range function stops one position before the last number
# so the upper limit is still 13

for province in range (0, 13):
	print (provinces_list[province])

print("")
print("")

# This loop print every other province starting with the first one 

for province in range (0, 13, 2):
	print (provinces_list[province])

print("")
print("")

# This loop print every other province starting with the second one 

for province in range (1, 13, 2):
	print (provinces_list[province])

print("")
print("")


