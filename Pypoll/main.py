import os
import csv

total_votes = 0
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0



file = "Resources/election_data.csv"
with open(file, "r") as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        total_votes +=1
        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham_votes +=1
      
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_votes +=1

candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_Casper_Stockham_votes, Diana_DeGette_votes, Raymon_Anthony_Doane_votes]

dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/total_votes) * 100  

Diana_DeGette_percent = (Diana_DeGette_votes/total_votes) * 100  

Raymon_Anthony_percent = (Raymon_Anthony_Doane_votes/total_votes) *100  

  

print("Election Results")
print("**********************************")
print(f"Total votes: {total_votes}")
print("**********************************")
print(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
print(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Raymon Anthony Doane: {Raymon_Anthony_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
print("*******************************")
print(f"Winner: {key}")

output_file = "Resources/Election_Results_Summary.txt"
with open(output_file, "w") as textfile:
    textfile.write("Election_Results_Summary.txt")
file.write(f"Election Results")
file.write("\n")
file.write(f"******************************")
file.write("\n")
file.write(f"Total Votes: {total_votes}")
file.write("\n")
file.write(f"********************************")
file.write("\n")
file.write(f"Charles Casper Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
file.write("\n")
file.write(f"Diana DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
file.write("\n")
file.write(f"Raymon Anthony Doane: {Raymon_Anthony_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
file.write("\n")
file.write(f"**********************************")
file.write("\n")
file.write(f"Winner: {key}")





    


    
