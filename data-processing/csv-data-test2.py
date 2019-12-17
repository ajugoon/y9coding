# A simple file that opens a CSV file and reads it line by line, which can then
# be printed, etc.

# import modules designed to process CSV files and handle error messages
import csv
import sys

all_nums = []

# defining a variable for the highest value in the list
def findMin(numArray):
    print ("min num is: ")
    min_value = 100.00
    for value in numArray:
        if value <= min_value:
            min_value = value
    return min_value

def findMax(numArray):
    print ("max num is: ")
    max_value = 0.00
    for value in numArray:
        if value >= max_value:
            max_value = value
    return max_value

def main():
    csv_file = open('data.csv')
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    try:
        # skip over the first line as these are just column headers
        next(csv_reader)
        for row in csv_reader:
            info = float(row[8])
            all_nums.append(info)
        
    except csv.Error:
        #sys.exit('file %s, line %d: %s' % ('data.csv', csv_reader.line_num, 'e'))
        print ("All Data Collected")
    
    finally:
        # in this block we execute any code that was not handled in the
        # 'try' block or the 'except' block
        # useful for closing objects and cleaning up resources
        
        # after we are done with any file we need to close it
        csv_file.close()
        print ("***")
        print (all_nums)
        print (findMin(all_nums))
        print (findMax(all_nums))
    

main()



