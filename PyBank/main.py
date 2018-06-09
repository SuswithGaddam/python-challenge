import os

# Module for reading CSV's
import csv

csvpath_1 = os.path.join('budget_data_1.csv')
csvpath_2 = os.path.join('budget_data_2.csv')

#Initialize variables to hold data
dates = []
num_of_months = 0
tot_rev = 0
past_rev = 0
change_inrev = []
avg_revchange = 0
amt_great_inc_rev = 0
amt_great_dec_rev = 0
dt_great_inc_rev = ''
dt_great_dec_rev = ''

with open(csvpath_1, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    #Skip Header
    Header = next(csvreader)
    #  Each row is read as a row
    for row in csvreader:
        dates.append(row[0])
        current_revenue = int(row[1])
        tot_rev = tot_rev + current_revenue
        rev_change = current_revenue - past_rev
        change_inrev.append(rev_change)
        past_rev = current_revenue

        if rev_change > amt_great_inc_rev:
            amt_great_inc_rev = rev_change
            dt_great_inc_rev  = row[0]
        
        if rev_change < amt_great_dec_rev:
            amt_great_dec_rev = rev_change
            dt_great_dec_rev = row[0]
        #print(row)
        
print(dates)
print(tot_rev)
print(change_inrev)
num_of_months = len(dates)
print(num_of_months)
print(amt_great_dec_rev)
print(dt_great_dec_rev)
print(amt_great_inc_rev)
print(dt_great_inc_rev)
