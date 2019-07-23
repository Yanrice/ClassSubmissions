import os
import csv


# opening ressource data
csvpath = os.path.join("Resources", "election_data.csv")

# def print_total(election_data_csv):
#     # For readability, it can help to assign your values to variables with descriptive names
#     candidate = str(election_data_csv[2])
#     voter_id = int(election_data_csv[0])
#     county = str(election_data_csv[1])
## List to store data : The dataset is composed of three columns: Voter ID, County, and Candidate
voter_id = []
candidate_count = 0
candidates = []
each_candidate = []
vote = []
vote_count = []
Percentage_vote_perc = []    

# Open and read csv
# Open and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:
      # total of vote in column
        candidate_count = candidate_count + 1
      # Set candidate name  
        candidates.append(row[2])
     # Set voter_id to Voter ID column
      #voter_id.append.(row[0])
     # Set county to column County
        county.append(row[1])
     # creat a new list for unique candidates
    for unique in set(candidates)
        each_candidate.append(unique)   
        # The total number of vote par candidates
        total_votes_perc = candidates.count(unique)
    
       percentage_vote = (total_votes_perc/candidate_count)*100
       Percentage_vote_perc.append(percentage_vote)
    # The winner is 
       most_vote_count = max(vote_count)
       most_vote_candidate = each_candidate[vote_count.index(most_vote_count)]

# Print the election result.
print("Election Results")   
print("------------------------------------")
print("Total Votes :" + str(canditate_count))    
print("------------------------------------")
# The total number of votes each candidate won
for i in range(len(unique_candidate)):

         print(each_candidate[i] + ": " + str( Percentage_vote_perc[i]) +"% (" + str(total_votes_perc[i])+ ")")

print("------------------------------------")
print("Winner: " +  most_vote_candidate)
print("------------------------------------")