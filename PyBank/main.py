#Homework #3 
#Revenue Analysis - Analyze financial records

# --------------------------------------------
#TE SPACE

# Part 0 - SETUP & Routing
# Allow user to create file paths using import os
import os

#Import Module for reading CSV files
import csv

#CSV is in 'Resources' folder (main is in same level as RS)
csvpath = os.path.join('Resources','budget_data.csv')

# Variable Storage
#p1
total_m = 0
#P2
net_totalpl = 0
#P3
av_changepl = 0
#P4
last_entry = 0
current_max = 0
#P5
current_min = 0


#Read CSV file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    #Skip Header
    next(csvreader,None)
   

# Part 1 - Total number of months included in the dataset
    #For Loop to go through each row of data (Cereal_Bonus_Solved)

    for row in csvreader:      
        #Part 1 Loop, add 1 with every row
        total_m += 1
        #Part 2 In each row, add value in column 1
        net_totalpl = int(row[1]) + net_totalpl
        #Part 4 create if then statement for Max
        if int(row[1]) - last_entry > current_max:
            # Assign current_max to the difference 
            current_max = int(row[1]) - last_entry
            # Pickup the date associated with this change
            current_max_date = row[0]
        
        
        #Part 5 create if then statement for minimum
        if int(row[1]) - last_entry < current_min:
            # Assign current_min to the difference
            current_min = int(row[1]) - last_entry 
            # Pickup the date associated with this change
            current_min_date = row[0]
        #Reset Last Entry for next loop
        last_entry = int(row[1])
    #Part 3 Average change is Total P/L over # of rows
    av_changepl = net_totalpl / total_m
    
    # Output Text
    #Print Header
    print("Financial Analysis")
    #Print Line Break
    print("-------------------")
    #P1
    print(f"Total Months: {total_m}")
    #P2
    print(f"Total: ${net_totalpl}")
    #P3
    print(f"Average Change: ${av_changepl}")
    #P4
    print(f"Greatest Increase in Profits: {current_max_date} (${current_max})")
    #P5
    print(f"Greatest Decrease in Losses: {current_min_date} (${current_min})")
    
#specify path to write to
data_output = os.path.join("Analysis","Results.txt")

#open outputfile to print everything above
with open(data_output, 'w',newline='') as txtfile:
            
    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow([f"Total Months: {total_m}"])
    csvwriter.writerow([f"Total: ${net_totalpl}"])
    csvwriter.writerow([f"Average Change: ${av_changepl}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {current_max_date} (${current_max})"])
    csvwriter.writerow([f"Greatest Decrease in Losses: {current_min_date} (${current_min})"])

    
# --------------------------------------------
# Part 2 - Net Total Amount of "Profit/Losses" over the entire period
    # Combine into original for loop, each row add value of second column
    # Save new value as net_totalpl
   


# --------------------------------------------
# # Part 3 - Average of changes in Profit/Losse over the entire period




# --------------------------------------------
# Part 4 - Greatest Increase in profits (date & amount) over the entire period
    # So we set a last entry value for value in col 1
    # Greatest increase involves || current entry - last Entry || > Current Max
    # Set Last Entry = 0 in beginning
    # Set Current_max =0 in beginning
    # in for loop set row[1] value to current entry
    # if loop to determine if row[1] - last_entry > current_max
        # if correct, assign current_max = row[1] - last_entry
            # save current_max_date as row[0]




# --------------------------------------------
# Part 5 - The Greatest decrease in losses (Date and amount) over the entire period




# --------------------------------------------
# FINAL -- Print to terminal & export a text file with results
# --------------------------------------------
# Sample Output
#Financial Analysis
# ----------------------------
#  Total Months: 86
#  Total: $38382578
# Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

