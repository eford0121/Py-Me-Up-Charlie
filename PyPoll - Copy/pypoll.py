import os
import csv

pollData = os.path.join("Resources", "election_data.csv")

total_votes = 0
khan_votes =0
correy_votes =0
li_votes = 0
otooley_votes =0




with open(pollData, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    for name in csvreader:
        if name[2] == "Khan":
            khan_votes += 1  
        elif name[2] == "Correy":
            correy_votes += 1 
        elif name [2] == "Li":
            li_votes += 1
        elif name [2] =="O'Tooley":
            otooley_votes +=1
        
        
#Determine total votes cast
total_votes = khan_votes + correy_votes + li_votes + otooley_votes  

#Determine percentages of total votes per candidate
khan_perc = (khan_votes / total_votes) *100 

correy_perc = (correy_votes/ total_votes)*100

li_perc = (li_votes / total_votes) *100

otooley_perc = (otooley_votes / total_votes) * 100     

if khan_votes> correy_votes and khan_votes> li_votes and khan_votes>otooley_votes:
    winner = " Khan!"
elif correy_votes>khan_votes and correy_votes>li_votes and correy_votes>otooley_votes:
    winner =" Correy!"
elif li_votes > khan_votes and li_votes > correy_votes and li_votes > otooley_votes :
    winner= " Li!"
elif otooley_votes > khan_votes and otooley_votes > correy_votes and otooley_votes > li_votes:
    winner -" O'Tooley!"




    
print ("Election Results")
print ("------------------------------")
print (f"Total Votes: " + str(total_votes))
print ("------------------------------")

print (f"Khan: " + str(round(khan_perc, 4)) + "% (" + str(khan_votes) + ")")
print (f"Correy: " + str(round(correy_perc, 4)) + "% (" + str(correy_votes) + ")")
print (f"Li: " + str(round(li_perc, 4)) + "% (" + str(li_votes) + ")")
print (f"O'Tooley: " + str(round(otooley_perc, 4)) + "% (" + str(otooley_votes) + ")")

print("-------------------------------")
print (f"Winner:" + (winner))
print ("------------------------------")
