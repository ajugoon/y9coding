# A simple file that opens a CSV file and reads it line by line, which can then
# be printed, etc.

# import modules designed to process CSV files and handle error messages
import csv
import sys

all_nums = []

# defining a variable for the highest value in the list

def main():
    csv_file = open('data.csv')
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    try:
        # skip over the first line as these are just column headers
        next(csv_reader)
        for row in csv_reader:
            info = float(row[8])
            all_nums.append(info)
            #print (all_nums)
            
    except csv.Error:
        #sys.exit('file %s, line %d: %s' % ('data.csv', csv_reader.line_num, 'e'))
        return "Error"
        
    # after we are done with any file we need to close it
    csv_file.close()

main()
print (all_nums)
print (len(all_nums))

