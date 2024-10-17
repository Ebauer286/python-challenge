# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
won_votes = 0 
total_won_votes = 0
popular_vote = 0

# Define lists and dictionaries to track candidate names and vote counts
candidates_dict = {}
candidates_list = []

# Winning Candidate and Winning Count Tracker
winner = ""
winning_count = 0
results = [] 

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        # print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1 

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidates_dict[candidate] = 0
        

        # Add a vote to the candidate's count
        candidates_dict[candidate] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(total_votes)

    # Write the total vote count to the text file
    txt_file.write(f'Total Votes: {total_votes}')

    # Loop through the candidates to determine vote percentages and identify the winner
    for key,value in candidates_dict.items():

        #Get the vote count and calculate the percentage
        key_candidate = int(candidates_dict[key])/total_votes * 100
        

        # Update the winning candidate if this one has more votes
        if winning_count < value: 
            winning_count = value
            winner = key

        # Print and save each candidate's vote count and percentage
        vote_output = f"{key}: {winning_count}, {key_candidate}%.2f " 
        print(vote_output)
        txt_file.write(vote_output)

    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
    # with open('election_results.txt', 'w') as txt_file:
    #     txt_file.write("Election Results\n") 
