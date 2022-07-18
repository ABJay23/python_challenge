import os
import csv



#lists to for iteration
total_months = []
total_profit = []
monthly_profit_change = []

#open file as csv and skip header
file = "budget_data.csv"
with open(file, "r") as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)

#iterate through rows that include months and profits
    for row in reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

#max and min profits calculations
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

#print results
print("Financial results")
print("***************************")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average change: {round(sum(monthly_profit_change)/len(monthly_profit_change), 2)}")
print(f"Greatest Increase in profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

output_file = os.path.join("python_challenge", "Pybank", "Financial_analysis_Summary.tx")
with opem(output_file, "w") as file:
    textfile.write(financial_results)






       

        
    