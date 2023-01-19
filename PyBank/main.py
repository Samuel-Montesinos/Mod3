import csv
import os

path = "PyBank/Resources"

months = 0
money_total = 0
big_profit = 0
little_profit = 0

with open('Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
#Skipping header row
    next(csv_reader) 

    #Calculating Numebers
    for row in csv_reader:
        months += 1
        money_total += int(row[1])
        if int(row[1]) > int(big_profit):
            big_profit = row[1]
            big_month = row[0]
        else:
            big_profit = big_profit
        if int(row[1]) < int(little_profit):
            little_profit = row[1]
            little_month = row[0]
        else: little_profit = little_profit

#calculating average
average = money_total/months
rounded_average = round(int(average), 2)

#Making Text Block
print("Financial Analysis")
print(" ")
print("------------------")
print(" ")
print(f'Total Months: {months}')
print(f'Total: ${money_total}')
print(f'Average Change: ${rounded_average}')
print(f'Greatest Increase in Profits: {big_month} (${big_profit})')
print(f'Greatest Decrease in Profits: {little_month} (${little_profit})')

#Creating and writing text file
array = [f'Financial Analysis\n', 
f'\n', 
f'------------------\n', 
f' \n', 
f'Total Months: {months}\n', 
f'Total: ${money_total}\n', 
f'Average Change: ${rounded_average}\n',
f'Greatest Increase in Profits: {big_month} (${big_profit})\n',
f'Greatest Decrease in Profits: {little_month} (${little_profit})\n']
with open('Analysis/Analysis.txt', 'w') as analysis:
    analysis.writelines(array)
