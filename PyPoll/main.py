import csv
import os

#Variables needed
tot_votes = 0
stock_votes = 0
deg_votes = 0
doa_votes = 0

with open('Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
#Skipping header row
    next(csv_reader) 
    
    #List of Candidates
    candidates = []
    for row in csv_reader:
        if row[2] not in candidates: #List of Candidates
            candidates.append(row[2])

with open('Resources/election_data.csv') as csv_file: 
    #Running again because admittedly I don't know how to append and
    #count without over extending my index
    csv_reader = csv.reader(csv_file, delimiter=',')
    #Skipping header row
    next(csv_reader) 
    for row in csv_reader: 
            #Counting Votes
        if row[2] == candidates[0]:
            stock_votes += 1
            tot_votes += 1
        if row[2] == candidates[1]:
            deg_votes += 1
            tot_votes += 1
        if row[2] == candidates[2]:
            doa_votes += 1
            tot_votes += 1
#Voting Total Calcs
stock_perc = 0.0 #Establishing Floats for %
deg_perc = 0.0
doa_perc = 0.0

stock_perc = (stock_votes / tot_votes) * 100
deg_perc = (deg_votes / tot_votes) * 100
doa_perc = (doa_votes / tot_votes) * 100

#Winner Calc
if stock_perc < deg_perc:
    winner = candidates[1]
    if deg_perc < doa_perc:
        winner = candidates[2]
else:
    if stock_perc < doa_perc:
        winner = candidates[2]
    else:
        winner = candidates[0]

#Prints
print('Election Results')
print('---------------------')
print(f'{candidates[0]}: {round(stock_perc, 3)}% ({stock_votes})')
print(f'{candidates[1]}: {round(deg_perc, 3)}% ({deg_votes})')
print(f'{candidates[2]}: {round(doa_perc, 3)}% ({doa_votes})')
print('---------------------')
print(f'Winner: {winner}')
print('---------------------')

#Creating and writing text file
array = [f'Election Results\n', 
f'---------------------\n', 
f'{candidates[0]}: {round(stock_perc, 3)}% ({stock_votes})\n',
f'{candidates[1]}: {round(deg_perc, 3)}% ({deg_votes})\n',
f'{candidates[2]}: {round(doa_perc, 3)}% ({doa_votes})\n'
f'---------------------\n'
f'Winner: {winner}\n'
f'---------------------\n']
with open('Analysis/Analysis.txt', 'w') as analysis:
    analysis.writelines(array)