Within this repo is the code meeting the parameters outlined for the Module 3 Challenge:

PyPoll Code:

    # Import necessary modules
    import csv
    import os
    
    # Files to load and output (update with correct file paths)
    file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
    file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path
    
    # Initialize variables to track the election data
    total_votes = 0  # Track the total number of votes cast
    
    # Define lists and dictionaries to track candidate names and vote counts
    candidate_names = []
    candidate_vote_count = {}
    # Winning Candidate and Winning Count Tracker
    winner = ""
    num_of_votes = 0
    
    # Open the CSV file and process it
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
  
      # Skip the header row
      header = next(reader)
  
      # Loop through each row of the dataset and process it
      for row in reader:
  
          # Print a loading indicator (for large datasets)
          print(". ", end="")
  
          # Increment the total vote count for each row
          total_votes += 1
  
          # Get the candidate's name from the row
          candidate_name = row[2]
  
          # If the candidate is not already in the candidate list, add them
          if candidate_name not in candidate_names:
              candidate_names.append(candidate_name)
  
          # Add a vote to the candidate's count
          if candidate_name in candidate_vote_count:
              candidate_vote_count[candidate_name] += 1
          else:
              candidate_vote_count[candidate_name] = 1
  
    # Open a text file to save the output
    with open(file_to_output, "w") as txt_file:
  
      # Print the total vote count (to terminal)
      print(" ")
      summary_starter = (
          f"Election Results\n"
          f"---------------------------\n"
          f"Total Votes: {total_votes}\n"
          f"---------------------------\n")
                
      # Write the total vote count to the text file
      txt_file.write(summary_starter)
      print(f"\n{summary_starter}")
  
      # Loop through the candidates to determine vote percentages and identify the winner
      for candidate, votes in candidate_vote_count.items():
  
          # Get the vote count and calculate the percentage
          vote_percentage = (votes / total_votes) * 100
  
          # Update the winning candidate if this one has more votes
          if votes > num_of_votes:
              num_of_votes = votes
              winner = candidate
  
          # Print and save each candidate's vote count and percentage
          candidate_result = f"{candidate}: {votes} votes ({vote_percentage: .3f}%)"
          print(candidate_result)
          txt_file.write(candidate_result + "\n")
  
      # Generate and print the winning candidate summary
      winning_summary = (f"---------------------------\n"
                      f"Winner: {winner}\n"
                      f"---------------------------\n")
      print(winning_summary)
      # Save the winning candidate summary to the text file
      txt_file.write(winning_summary + "\n")


PyBank Code:

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
