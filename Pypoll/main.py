import os
import csv

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


file = "election_data.csv"
with open(file, "r") as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        total_votes +=1
        if row[2] == "khan":
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "li":
            li_votes +=1
        elif row[2] == "O'Tooley":
            otoolety_votes +=1

candidates = ["khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

khan_percent = (khan_votes/total_votes) * 100  

correy_percent = (correy_votes/total_votes) * 100  

li_percent = (li_votes/total_votes) *100  

otooley_percent = (otooley_votes/total_votes) * 100  

print("Election Results")
print("**********************************")
print(f"Total votes: {total_votes}")
print("**********************************")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"correy: {correy_percent:.3f}% ({correy_votes})")
print(f"li: {li_percent:.3f}% ({li_votes})")
print(f"otooley: {otooley_percent:.3f}% ({otooley_votes})")
print("*******************************")
print(f"Winner: {key}")

output_file = Path("Election_Results_Summary.txt")
file.write(f"Election Results")
file.write("\n")
file.write(f"******************************")
file.write("\n")
file.write(f"Total Votes: {total_votes}")
file.write("\n")
file.write(f"********************************")
file.write("\n")
file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
file.write("\n")
file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
file.write("\n")
file.write(f"Li: {li_percent:.3f}% ({li_votes})")
file.write("\n")
file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
file.write("\n")
file.write(f"**********************************")
file.write("\n")
file.write(f"Winner: {key}")





    


    
