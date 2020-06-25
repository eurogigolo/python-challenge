import os
import csv
import statistics

#task 1.1
dates = []
number_months = 0

#task 1.2
total = 0
profitlist = []

#task 1.3
change = []


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath,'r')as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    

    
    for row in csvreader:
        number_months = number_months + 1 #adds 1 for every row in csv

        dates.append(row[0]) #adds all dates to empty list

        total = int(row[1]) + total #sums the total profit/loss clumns
        
        
        profitlist.append(int(row[1]))#adds all profits and losses to list
        maxgreatest = max(profitlist)#max value of the list
        minleast = min(profitlist)#min value of list

        mean1 = statistics.mean(profitlist)
        change.append(int(row[1]) - mean1)
        changetotal = round(statistics.mean(change),2)


        if int(row[1]) == maxgreatest:#determines the date of the great profit or loss
            greatdate = row[0]
        elif int(row[1]) == minleast:
            leastdate = row[0]




    print("Financial Analysis")
    print("--------------------------")
    print(f"Total Months: {number_months}")
    print(f"Total Profit: ${total}")
    print(f"Average Change: ${changetotal}")
    print(f"Greatest Increase in Profits: {greatdate} (${maxgreatest})")
    print(f"Greatest Decrease in Profits: {leastdate} (${minleast})")

    file = open('analysis/pythonhw.txt','w')

    file.write("Financial Analysis\n")
    file.write("--------------------------\n")
    file.write(f"Total Months: {number_months}\n")
    file.write(f"Total Profit: ${total}\n")
    file.write(f"Average Change: ${changetotal}\n")
    file.write(f"Greatest Increase in Profits: {greatdate} (${maxgreatest})\n")
    file.write(f"Greatest Decrease in Profits: {leastdate} (${minleast})\n")




        


