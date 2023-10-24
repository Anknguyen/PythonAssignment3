import pandas as pd

#Reading info from csv files
dataFrame1 = pd.read_csv('pythonassignment3-main/resources/election_data.csv')
dataFrame2 = pd.read_csv('pythonassignment3-main/resources/budget_data.csv')



#PyBank
#Sorting dataframe
date = dataFrame2.loc[:,'Date']
profitLoss = dataFrame2.loc[:,'Profit/Losses']

#Number of months
months = len(date)

#Total profits/losses
totalProfitLoss = sum(profitLoss)

#Finding the greatest increase in profits
maxId = dataFrame2[['Profit/Losses']].idxmax()
increase = dataFrame2.loc[maxId,:]

#Finding the greatest decrease in profits
minId = dataFrame2[['Profit/Losses']].idxmin()
decrease = dataFrame2.loc[minId,:]

#Finding the average
average = totalProfitLoss/months


#PyDoll
#Total Votes
numVotes = len(dataFrame1)

#List of Candidates
candidateDf = dataFrame1.drop_duplicates(subset=['Candidate'])
candidate = candidateDf.loc[:,'Candidate']

#Total number of votes
totalVotes = dataFrame1['Candidate'].value_counts()
diana = totalVotes['Diana DeGette']
charles = totalVotes['Charles Casper Stockham']
raymon = totalVotes['Raymon Anthony Doane']

#Percentage of votes
dianaP = round((diana/numVotes) * 100,2)
charlesP = round((charles/numVotes) * 100,2)
raymonP = round((raymon/numVotes) * 100,2)

#Winner
winner = totalVotes.idxmax()


fileWrite = "Financial Analysis\n------------------ \n" + "Total Months: " + str(months) +"\n" + "Total: " + str(totalProfitLoss) + "\n" + "Average Change: " + str(average) + "\n" + "Greatest Increase in Profits: " + str(increase) + "\n" + "Greatest Decrease in Profits" + str(decrease) + "\n" + "\n" + "Election Results\n------------------ \n" + "Total Votes: " + str(numVotes) + "\n" + "Charles Casper Stockham: " + str(charlesP) + "% " + str(charles) + "\n" + "Diana DeGette: " + str(dianaP) + "% " + str(diana) + "\n" + "Raymon Anthony Doane: " + str(raymonP) + "% " + str(raymon) + "\n" + "Winner is: " + winner

#Opening text file
file = open("pythonassignment3-main/Analysis/analysis_data.txt", "w")
file.write(fileWrite)