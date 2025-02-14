import csv
import os

#assign variable for data load and the path
data = os.path.join('Resources', '2018-19_pbp.csv')

#initialize total row count
total_rows = 0
#initialize team list
teams = []
#create player list
players = []

#open NBA data
with open(data) as NBA_2018_2019:
    #read the file
    NBA_read = csv.reader(NBA_2018_2019)
    #print the header row 
    headers = next(NBA_read)

    #create a total count of data rows
    for row in NBA_read:
        #add to total row count
        total_rows += 1

        #TEAM DATA
        #where to find the abbreviation field
        team_abb = row[14]

        #if team name does not match existing team..
        if team_abb not in teams:
            #add team to list
            teams.append(team_abb)
        
        #PLAYER DATA
        #where to find player name
        player_name = row[13]

        #if player name does not match existing player..
        if player_name not in players:
            #add player to list
            players.append(player_name)

#print header row
print(headers) 
#print unique team list
print(teams)
#print unique player list
print(players)