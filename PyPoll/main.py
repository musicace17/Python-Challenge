# Import modules to use
import os
import csv

# Path the CSV to be used in the code
csvpath = os.path.join("Resources", "election_data.csv")

# Set up list variables to store the 3 columns' data into
Ballot_ID = []
County = []
Candidate = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header before storing the column data
    csvhead = next(csvreader)

    # Log the data of each column to their respective variable
    for row in csvreader:
        Ballot_ID.append(row[0])
        County.append(row[1])
        Candidate.append(row[2])


    # Print the header to the results to be printed
    print("") # adding some space before printing results in the terminal
    print("Election Results")
    print("----------------------------")

    # Count the number of ballots in the file and print result
    vote_count = len(Ballot_ID)
    print("Total Votes: " + str(vote_count))
    print("----------------------------")


    # Count the number of appearances of each candidate name in the Candidate column, store as new variable, and append to a new list
    can_count = []
    can1count = Candidate.count("Charles Casper Stockham")
    can_count.append(can1count)
    can2count = Candidate.count("Diana DeGette")
    can_count.append(can2count)
    can3count = Candidate.count("Raymon Anthony Doane")
    can_count.append(can3count)


    # Store unique runner names into a new list
    Runners = []
    for person in Candidate:
        if person not in Runners:
            Runners.append(person)


    # Do math with these variables and the vote_count to get percentages, round to nearest 3 decimals, and append to a new list
    can_percentages = []
    can1percent = can1count / vote_count * 100
    can1percent = round(can1percent, 3)
    can_percentages.append(can1percent)
    
    can2percent = can2count / vote_count * 100
    can2percent = round(can2percent, 3)
    can_percentages.append(can2percent)

    can3percent = can3count / vote_count * 100
    can3percent = round(can3percent, 3)
    can_percentages.append(can3percent)

    # Print the results via f strings
    print(f"{Runners[0]}: {can1percent}% ({can1count})")
    print(f"{Runners[1]}: {can2percent}% ({can2count})")
    print(f"{Runners[2]}: {can3percent}% ({can3count})")
    print("----------------------------")

    # Find the winner and print the result
    winner = Runners[can_percentages.index(max(can_percentages))]
    print("Winner: " + str(winner))
    print("----------------------------")

    # Print results to a text file
    # Open the file
    with open(os.path.join("Analysis", "analysis_results.txt"), "w+") as resultxt:
        # Write the lines of the file
        resultxt.write("Election Results")
        resultxt.write("\n----------------------------")
        resultxt.write("\nTotal Votes: " + str(vote_count))
        resultxt.write("\n----------------------------")
        resultxt.write(f"\n{Runners[0]}: {can1percent}% ({can1count})")
        resultxt.write(f"\n{Runners[1]}: {can2percent}% ({can2count})")
        resultxt.write(f"\n{Runners[2]}: {can3percent}% ({can3count})")
        resultxt.write("\n----------------------------")
        resultxt.write("\nWinner: " + str(winner))
        resultxt.write("\n----------------------------")
        #Close the file
        resultxt.close