
# Module for reading CSV files
import os
import csv

# Declare Variables to resolve
total_votes=0
candidates=[]
cnt_votes=[]



#Loading the csv file for fact finding

csvpath = os.path.join('Data_Source/election_data.csv')
with open(csvpath, newline='') as election_data:

    # CSV reader specifies delimiter and variable that holds contents
    election_reader = csv.reader(election_data, delimiter=',')
    print(election_reader)

    # Excluding the header
    csv_header = next(election_reader)
    for row in election_reader:

    #Get total votes
        total_votes=total_votes + 1 
        
    #Adding count to the candidate list
        candidate=row[2]
        if candidate in candidates:
           candidate_one = candidates.index(candidate)
           cnt_votes[candidate_one]=cnt_votes[candidate_one]+1
    # If not then create a list for another candidate#
        else:
            candidates.append(candidate)
            cnt_votes.append(1)


#Counting the percentages and  counts
percentages = []
votes_max = cnt_votes[0]
index_max = 0


#find percentage of vote for each candidate and the winner
for count in range(len(candidates)):
    vote_percentage = round(cnt_votes[count]/total_votes*100,3)
    
    percentages.append(vote_percentage)
    if cnt_votes[count] > votes_max:
        votes_max = cnt_votes[count]
        print(votes_max)
        index_max = count
winner = candidates[index_max]

#print results
print("-----------------------------")
print("Election Results Summary")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({cnt_votes[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")



#Output File
export_file = os.path.join("PyPoll Election Summary Results.txt")
with open(export_file,'w',newline="") as NewSummary:
    NewSummary.write("-----------------------------\n")
    NewSummary.write("Election Results Summary\n")
    NewSummary.write("-----------------------------\n")
    NewSummary.write(f"Total Votes: {total_votes}\n")
    NewSummary.write("-----------------------------\n")
    for count in range(len(candidates)):
        NewSummary.write(f"{candidates[count]}: {percentages[count]}% ({cnt_votes[count]})\n")
    NewSummary.write("-----------------------------\n")
    NewSummary.write(      f"Winner: {winner}\n")
    NewSummary.write("-------END REPORT------------\n")


    NewSummary.write.close()
