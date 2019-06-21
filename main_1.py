import os
import csv

#Reading data from the file budget_data.csv
csvpath = os.path.join("Data_Source/budget_data.csv")
with open(csvpath, 'r', newline='') as budget_data:    
    
    budget_reader= csv.reader(budget_data, delimiter=',')
    #Reading header
    csv_header = next(budget_reader)

    #Initializing variables and lists values
    dates_month = []
    total_net_rev = 0
    maxProfit = 0
    minProfit = 0
    
    #Looping through each data record in the file
    for row in budget_reader:
        dates_month.append(row[0])
        #Summing up the revenue for each month
        total_net_rev += int(row[1])

        #Calculating the maximum profit and month
        if(maxProfit<int(row[1])):
            maxProfit = int(row[1])
            maxProfitMonth = row[0]
        
        #Calculating the minimum profit or maximum loss
        if(minProfit>int(row[1])):
            minProfit = int(row[1])
            minProfitMonth = row[0]
    
    #Printing output on console
    print("\nFinancial Analysis\n-----------------------------------------------")
    print(f"Total Month: {len(dates_month)}")
    print(f"Total Revenue : ${total_net_rev}")
    print(f"Average Change : ${round(total_net_rev/len(dates_month),2)}")
    print(f"Greatest Increase in Profits : {maxProfitMonth} ({maxProfit})")
    print(f"Greatest Decrease in Profits : {minProfitMonth} ({minProfit})")



#Exporting Output file

newfile = open('output.txt','w')
newfile.write("Financial Analysis")
newfile.write("\n-----------------------------------------------")
newfile.write("\nTotal Month: " + str(len(dates_month)))
newfile.write("\nTotal Revenue : $" + str(total_net_rev))
newfile.write("\nAverage Change : $" + str(round(total_net_rev/len(dates_month),2)))
newfile.write("\nGreatest Increase in Profits : " + str(maxProfitMonth) + " (" + str(maxProfit) + ")")
newfile.write("\nGreatest Decrease in Profits : " + str(minProfitMonth) + " (" + str(minProfit) + ")")

newfile.close()