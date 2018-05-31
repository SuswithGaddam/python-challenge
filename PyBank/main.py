import os

# Module for reading CSV's
import csv

csvpath_1 = os.path.join('..', 'Resources', 'budget_data_1.csv')
csvpath_2 = os.path.join('..', 'Resources', 'budget_data_2.csv')
csvpath = [csvpath_1,csvpath_2]

# # Method 1: Plain Reading of CSVs
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #  Each row is read as a row
    for row in csvreader:
        #print(row)
