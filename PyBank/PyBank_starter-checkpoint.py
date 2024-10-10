# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 1
total_net = 0
# Add more variables to track other necessary financial data
grtst_inc = ["",0]
grtst_dec = ["",0]
net_change_list = []
avg_change = 0
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    
    # Track the total and net change
    total_net += int(first_row[1])  
    previous_net = (first_row[1])
    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        # Track the net change
        current_net = int(row[1])
        total_net += current_net
        net_change = int(current_net - int(previous_net))
        net_change_list.append(net_change)
        previous_net = current_net
        # Calculate the greatest increase in profits (month and amount)
        if net_change > grtst_inc[1]:
            grtst_inc = [row[0], net_change]
        # Calculate the greatest decrease in losses (month and amount)
        if net_change < grtst_dec[1]:
            grtst_dec = [row[0], net_change]


# Calculate the average net change across the months
avg_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
analysis_summary = (
f"Financial Analysis\n"
f"---------------------\n"
f"Total Months: {total_months}\n"
f"Total: ${total_net}\n"
f"Average Change: ${avg_change:.2f}\n"
f"Greatest Increace in Profits: {grtst_inc[0]} (${grtst_inc[1]})\n"
f"Greatest Decrease in Losses: {grtst_dec[0]} (${grtst_dec[1]})\n"
)
# Print the output
print(analysis_summary)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(analysis_summary)
