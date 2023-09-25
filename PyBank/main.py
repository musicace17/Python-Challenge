# Import modules to use
import os
import csv

# Path the CSV to be used in the code
csvpath = os.path.join("Resources", "budget_data.csv")

# Set up some variables to store the 2 columns' data into
Date = []
Change = []

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header before doing any calculations
    csvhead = next(csvreader)

    # Log the data of each column to their respective variable
    for row in csvreader:
        Date.append(row[0])
        Change.append(row[1])


    # Print the header to the results to be printed
    print("") # this is to add a little space before printing results in the terminal
    print("Financial Analysis")
    print("----------------------------")

    # Count the number of months in the file and print result
    Date_count = len(Date)
    print("Total Months: " + str(Date_count))

    # Convert the "Change" list to be a list of integers instead of strings
    Change_int = [eval(x) for x in Change]
   
    # Sum the profit/losses column and print result
    Net_profloss = sum(Change_int)
    print("Total: $" + str(Net_profloss))

    # Create a mean function to call later
    def mean(set):
        return sum(set) / len(set)

    # Store changes in a list by looping through the profit/losses column and subtracting the preceding row from the current
    Changes = []
    for i in range (1, len(Change_int)):
        change = Change_int[i] - Change_int[i-1]
        Changes.append(change)
    
    # Find the average of the Changes list and round to the nearest 2 decimals
    change_result = mean(Changes)
    change_result = round(change_result, 2)
    print("Average Change: $" + str(change_result))

    # Find the max and min values in the Changes list and apply the index of found values to find the date
    Greatinc = max(Changes)
    Incindex = Changes.index(Greatinc)
    Incdate = Date[Incindex + 1]
    print(f"Greatest Increase in Profits: {Incdate} (${Greatinc})")

    Greatdec = min(Changes)
    Decindex = Changes.index(Greatdec)
    Decdate = Date[Decindex + 1]
    print(f"Greatest Decrease in Profits: {Decdate} (${Greatdec})")

    # Print results to a text file
    # Open the file
    with open(os.path.join("Analysis", "analysis_results.txt"), "w+") as resultxt:
        # Write the lines of the file
        resultxt.write("Financial Analysis")
        resultxt.write("\n----------------------------")
        resultxt.write("\nTotal Months: " +str(Date_count))
        resultxt.write("\nTotal: $" +str(Net_profloss))
        resultxt.write("\nAverage Change: $" +str(change_result))
        resultxt.write(f"\nGreatest Increase in Profits: {Incdate} (${Greatinc})")
        resultxt.write(f"\nGreatest Decrease in Profits: {Decdate} (${Greatdec})")
        # Close the file
        resultxt.close()