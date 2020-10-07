#Import the useful modules
import os
import csv

#create empty list to store the data needed
voterID = []
county = []
candidate = []

#Import the data from the csv file
filePath = os.path.join("Resources", "election_data.csv")
with open(filePath) as csvfile:
    elecData = csv.reader(csvfile, delimiter = ",")
    
    #returns the header and start the rows on the next row
    csv_header = next(elecData)
    
    # Assign the row to the empty lists  pre-defined above
    for row in elecData:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

#Unique candidate list
unicand = [] 
count = 0

#loop for count and find the unique candidates in the candidate
for i in range(len(voterID)):
    count += 1
    if i < len(voterID)-1:
        if candidate[i] != candidate[i+1] and candidate[i] not in unicand:
            unicand.append(candidate[i])

#create the numVotes list to retriev the number of votes per candidate
numVotes = [0] * len(unicand)

#loop to calculate the votes per candidate and store in the list
for x in candidate :
    if x in unicand:
        index = unicand.index(x)
        numVotes[index] = numVotes[index] + 1

#Summary data 
count = str(count)
percent = []
listvotespercandidate = []

#loop through the 3 lists unicand, numVotes and percent to put them together in 1 list
for i in range(len(unicand)):
    percent.append(numVotes[i]/int(count)*100)
    listvotespercandidate.append(f"{unicand[i]} : {round(percent[i],1)}% ({numVotes[i]})")

#Find the winner with the highest percent    
maxpercent = max(percent)
indexmaxpercent = percent.index(maxpercent)
winner = unicand[indexmaxpercent]

#print the result in the analysis text file
output_path = os.path.join("analysis", "analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.writelines(["Election Results",
                    "\n------------------------",
                    "\nTotal Votes: " + count,
                    "\n-----------------------\n",
                    '\n'.join(listvotespercandidate),
                    "\n-----------------------",
                    "\nWinner : " + winner,
                    "\n-----------------------"])

#Print the results form the text file in the terminal
with open(output_path, 'r') as analysis:
    for line in analysis:
        print(line.strip())
    