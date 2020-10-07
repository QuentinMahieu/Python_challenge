# import the data from the cvs file
import os
import csv

#create empty lists
dates = []
profitLoss = []
changeslist = []

#Python_challenges as workdirectory yo be able to read the file
filePath = os.path.join("Resources", "budget_data.csv" )
with open(filePath, 'r') as csvfile :
    budgetData = csv.reader(csvfile, delimiter = ",")

#Assign the header and move to the next row for the rest of the script
    csv_header = next(budgetData)

# Assigns the rows in the empty lists created
    for row in budgetData :
        dates.append(row[0])
        profitLoss.append(row[1])

#Transform the profitLoss str list in an int list. Assign the changes in the changelist 
for i in range(len(profitLoss)):
    profitLoss[i] = int(profitLoss[i])
    if i < len(profitLoss)-1:
        changeslist.append(int(profitLoss[i+1])- profitLoss[i])

#summary table
months = str(len(dates))
total = str(sum(profitLoss))
avgchanges = str(round(sum(changeslist) / (len(profitLoss)-1),2))
maxchange = max(changeslist)
minchange = min(changeslist)

#Find the dates of max and min with
maxindex = changeslist.index(maxchange)
minindex = changeslist.index(minchange)
datemax = dates[maxindex +1] #the changelist is from lenght -1 compare to the date list; +1 to have the correct index in the date list
datemin = dates[minindex +1]

# Print the results in a text file
output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.writelines(["Financial Analysis", 
                "\n-----------------------",
                "\nTotal Months : " + months,
                "\nTotal : $" + total,
                "\nAverage Change : $" + avgchanges ,
                f"\nGreatest Increase in Profits : {datemax} $({maxchange}) " ,
                f"\nGreatest Decrease in Profits : {datemin} $({minchange}) "])

#Print the results from the analysis file in the terminal
with open(output_path, 'r') as analysis:
    for line in analysis:
        print(line.strip())
