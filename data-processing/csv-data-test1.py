# A simple file that opens a CSV file and reads it line by line, which can then
# be printed, etc.

# import modules designed to process CSV files and handle error messages
import csv
import sys

def main():
    csv_file = open('data.csv')
    csv_reader = csv.reader(csv_file, delimiter = ',')
    
    # our first attempt to doing some error checking
    # "try" means that we will execute this block first

    try:
        # skip over the first line as these are just column headers
        next(csv_reader)
        for row in csv_reader:
            # first column will be column "0"
            print (row[8])

    # "except" refers to the block of code that will generate an error message
    # if any issues are detected such as when we reach the end of the file and there
    # is no more data to pull
    except csv.Error:
        sys.exit('file %s, line %d: %s' % ('data.csv', csv_reader.line_num, 'e'))
        return "Error"
    # after we are done with any file we need to close it
    csv_file.close()

main()
