# import libraries
import os
import csv

# setting path
budgetCsv =  os.path.join('Resources', "budget_data.csv")

# variables
months =[]
profit=[]


# reading the file 
with open(budgetCsv, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    
    # counting months; finding total revenue; find greatest inc & dec in revenue
    for row in csvreader:
        months.append(row[0])
        profit.append (int(row[1]))

        total_months = len(months)

        greatest_inc = profit[0]
        greatest_dec = profit[0]

    for info in range(len(profit)):
        if profit[info] == int(max(profit)):
            greatest_inc = profit[info]
            greatest_inc_mn = months[info]
        elif profit[info] == int(min(profit)):
            greatest_dec= profit[info]
            greatest_dec_mn = months[info]
        
total_profit = int(sum(profit))


#Print analysis
print ("Financial Analysis")
print("---------------------------")
print (f"Total Months: " + str(total_months))
print (f"Total Profit: $" +str(total_profit))
print (f"Average Change: $")) #Could not figure this part out. Sorry!
print (f"Greatest Increase in Profits: " + str(greatest_inc_mn) + " ($" + str(greatest_inc)+ ")")
print (f"Greatest Increase in Profits: " + str(greatest_dec_mn) + " ($" + str(greatest_dec)+ ")")