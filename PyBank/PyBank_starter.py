# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
profit_loss = 0
profit_gain = 0
total_profit_loss = 0
previous_month = 0
average_change = 0
#greatest_increase = 0 
#greatest_decrease = 0 
net_change = []
greatest_increase = [" " , 0] 
greatest_decrease = [" " , 9999999]

# Open and read the csv
with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    

    # Skip the header row
    header = next(csvreader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(csvreader) 
    total_net += int(first_row[1]) 
    total_months += 1
    previous_month = int(first_row[1])

    # Track the total and net change
    

    # Process each row of data
    for row in csvreader:

        # Track the total
        total_months += 1
        profit_loss = int(row[1])
        total_profit_loss += profit_loss

        # Track the net change
        net_change_tracker = int(row[1]) - previous_month
        net_change += [net_change_tracker]
        previous_month = int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        if net_change_tracker > greatest_increase[1]:
            greatest_increase[1] = net_change_tracker
            greatest_increase[0] = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change_tracker < greatest_decrease[1]:
            greatest_decrease[1] = net_change_tracker
            greatest_decrease[0] = row[0]


# Calculate the average net change across the months
average_change = sum(net_change) / len(net_change) 

# Generate the output summary


# Print the output
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss + total_net}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: ${greatest_increase}')
print(f'Greatest Decrease in Profits: ${greatest_decrease}')

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f'Total Months: {total_months}')
    txt_file.write(f'Total: ${total_profit_loss + total_net}')
    txt_file.write(f'Average Change: ${average_change:.2f}')
    txt_file.write(f'Greatest Increase in Profits: ${greatest_increase}')
    txt_file.write(f'Greatest Decrease in Profits: ${greatest_decrease}')