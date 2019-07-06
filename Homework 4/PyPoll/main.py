import os
import csv

## List to store data : The dataset is composed of three columns: Voter ID, County, and Candidate
voter_id = []
county = []
candidate = []
vote = []
Percentage_vote = []
# opening ressource data
csvpath = os.path.join("..", "Resources", "election_data.csv")

# def print_total(election_data_csv):
#     # For readability, it can help to assign your values to variables with descriptive names
#     candidate = str(election_data_csv[2])
#     voter_id = int(election_data_csv[0])
#     county = str(election_data_csv[1])
    

# Open and read csv
with open(csvpath, newline="") as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
        
        # total of vote in column

        # voter_id.append.(column[0])
        # # Add price
        # county.append(colum[1])
        # # Add titlen
        # candidate.append(column[2])
        # The total number of votes cast
    # vote_total = 0.0
    # for vote in Voter_ID:
    #     vote_total += Voter_ID
    # return vote_total / length

# The percentage of votes each candidate won 2 decimal place
# percent = round(int(column[1]) /total_number_vote, 2)
#         review_percent.append(percent)

# The total number of votes each candidate won

# # The winner of the election based on popular vote.
# print("Total Votes: " + str(vote_total))
# # Prints a statement adding the variable
# print("Nick is a professional " + title)

# # Convert the integer years into a string and prints
# print("He has been coding for " 