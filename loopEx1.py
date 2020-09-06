# Loop Example # 1
# The "For Loop" performs a task a finite number of times and then stops.

# If we choose not to use a loop we can copy-and-paste the command we wish to 
# execute as many times as needed. This technique works, but is very inefficient 
# especially for large numbers of occurences

print ("Here we can print multiple times without using the Loop")

print ("hello")
print ("hello")
print ("hello")
print ("hello")
print ("hello")

print ("")
print ("")

# Here we use the FOR Loop

print ("Now we can get the same outcome with using the Loop")

for x in range(0, 5):
	print ("hello")
