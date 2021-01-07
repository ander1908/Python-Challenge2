#LETS GET DOWN TO BUSINESS
#TE Area
#------------------------------------
#Part 0 Setup
# Allow user to create file paths using import os
import os

#Import Module for reading CSV files
import csv

import numpy as np


#CSV is in 'Resources' folder (main is in same level as RS)
csvpath = os.path.join('Resources','election_data.csv')

# Variable Storage
#P1 
total_vote = 0
#P2
votes = []
#P3
c0_count = 0

#Read CSV file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')
    #Skip Header
    csv_header = next(csvreader)

    #Part 2 candidate read
  
    for row in csvreader:
        #part 1 Total Vote
        total_vote += 1
        #part 2 if Loop storing unique Values
        votes.append(row[2])
        
        #Part 3
    votes_unique = np.unique(votes)         
    #Part 1 I could use total vote avlue, or length of list from votes
    #print(votes_unique)
    #print(total_vote)
    #print(len(votes))
    
    # PRINTING CENTER
    # Write the first row (column headers)
    print('Election Results')
    print('-------------------')
    print(f"Total Votes: {total_vote}")
    print('-------------------')
    
    # WELL IN HOUR 15 I find something that works
    #https://www.tutorialspoint.com/count-frequencies-of-all-elements-in-array-in-python
    #THANK THE LORD
    #I created the votes array which took all of the votes and put them into a list
    #I created an empty dict to hold candidate count
    #So looking through the votes list, if I didn't find it, set value to 1, otherwise increase
    candidate_count = {}
    max = 0
    for candidates in votes:
        if candidates in candidate_count:
            candidate_count[candidates] += 1
        else:
            candidate_count[candidates] = 1
    #Printing the values for the individual items
    for key, value in candidate_count.items():
        print(f"{key}: {round((value/total_vote)*100,2)}% ({value})")
    #For Printing Winner. Set Max for values, if anything surpasses it, it will be new max and its key will be winner
    print('-------------------')    
    for key, value in candidate_count.items():
        if value > max:
            print(f"Winner: {key}")
            max = value
            winner = key
    print('-------------------')
    
    #DISREGARD BELOW
    #Candidate Assignment based on unique values 
    #candidate_0 = votes_unique[0]
    #print(votes_unique[0])
    #print(f"{votes_unique[0]}")
    #candidate_1 = votes_unique[1]
    #print(f"{votes_unique[1]}")
    #candidate_2 = votes_unique[2]
    # print(f"{votes_unique[2]}")
    #candidate_3 = votes_unique[3]
    #print(f"{votes_unique[3]}")
    
    #CALCULATION CENTER FOR

    #Candidate_0
    #use for loop to attribute all candidates to counts
    
    
    
    
    
#specify path to write to
data_output = os.path.join("Analysis","Results.txt")

#open outputfile to print everything above
with open(data_output, 'w',newline='') as txtfile:
            
    # Initialize csv.writer
    csvwriter = csv.writer(txtfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow([f"Total Votes: {total_vote}"])
    csvwriter.writerow(['-------------------'])
    for key, value in candidate_count.items():
        csvwriter.writerow([f"{key}: {round((value/total_vote)*100,2)}% ({value})"])
    
    #csvwriter.writerow([f"{candidate_1}: "])
   # csvwriter.writerow([f"{candidate_2}: "])
    #csvwriter.writerow([f"{candidate_3}: "])
    csvwriter.writerow(['-------------------'])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(['-------------------'])
    #Test Script
    #print(votes)
       
#Part 1 Total Number of Votes Cast
    #for loop counting the rows iterating total vote count
    # total_vote += 1
    #print(f"Total Votes: {total_vote}")
#------------------------------------
#Part 2 Complete List of Candidates who received votes
    #Create empty list in variable storage
    #Needs to pull unique values to amend to list
    #then print list
    # using https://www.geeksforgeeks.org/python-get-unique-values-list/
    # numpy function
    # UDPATE - https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
    # Set to slim down 
#------------------------------------
#Part 3 Percentage of Votes each candidate won
    #Sum by unique candidate, divide by total Votes
    #Create new column for this value
#------------------------------------
#Part 4 Total number of votes each candidate won
    #sum of votes for each candidate
    #Create new column
#------------------------------------
#Part 5 The winner of the election based on popular vote
    #if statement comparing each sequential Total vote # against the next
    #print victor's name
    #print(f"Winner: {victor}")
#------------------------------------
# THEN CLAIM ELECTION FRAUD IF YOUR CANDIDATE LOSES. IT IS THE WAY

#PRINT TO TEXT FILE WITH RESULTS
#EXAMPLE
# Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------