#Import dependencies
import os
import csv

#Set variable for csv path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row 
    csv_header = next(csvreader)
    print (csv_header)
    for row in csvreader:
        print(row)

#Set Variables
TotalMonths = 0
Total = 0
NetProfitLosses = 0
ProfitLossChange = 0

TotalMonths = (len(Date))
TotalMonths

