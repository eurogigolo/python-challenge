import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath,'r')as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    #header = next(csvreader)
    
    #task 1.1
    number_months = 0
    #task 1.2
    total = 0
    #task 1.3
    profitlist = []
    change = 0
    changetotal = 0
    for row in csvreader:
        number_months = number_months + 1
        total = int(row['Profit/Losses']) + total

        greatestincrease = max(row['Profit/Losses'])
        greatestdecrease = min(row['Profit/Losses'])
        increasedate = []
        decreasedate = []

        #print(row['Profit/Losses'])
        if row['Profit/Losses'] == greatestincrease:
            increasedate.append(row['Date'])
        if row['Profit/Losses'] == greatestdecrease:
            decreasedate.append(row['Date'])
        #change = row - (row + 1)) + change
        #changetotal = change / number_months


    print(f"Total Months: {number_months}")
    print(f"Total Profit: ${total}")
    #print(f"Average Change: ${change}")
    print(f"Greatest Increase in Profits: {increasedate}({greatestincrease})")
    print(f"Greatest Increase in Profits: {decreasedate} ({greatestdecrease})")




        


