import csv
import os

#assign variable for data load and the path
data = os.path.join('Resources', '2018-19_pbp.csv')

#initialize total row count
#total_rows = 0
#initialize team list
teams = []
team_total = 0
#create player list
players = []
player_total = 0
player_dir = {}
#create game list
games = []
game_total = 0

#open NBA data
with open(data) as NBA_2018_2019:
    #read the file
    NBA_read = csv.reader(NBA_2018_2019)
    #print the header row 
    headers = next(NBA_read)

    #create a total count of data rows
    for row in NBA_read:
        #add to total row count
        #total_rows += 1

        #TEAM DATA
        #where to find the abbreviation field
        team_abb = row[14]

        #if team name does not match existing team..
        if team_abb not in teams:
            #add team to list
            teams.append(team_abb)
            team_total += 1
        
        #PLAYER DATA
        #where to find player name
        player_name = row[13]
        player_type = row[9]

        #if player name does not match existing player..
        if player_name not in players:
            #add player to list
            players.append(player_name)
            player_total += 1
 
        #add to player and team to directory
        if player_name not in player_dir:
            player_dir[player_name,team_abb] = 1
       
        #GAME DATA
        #where to find game id
        game_id = row[4]
        
        #if game id does not match existing game
        if game_id not in games:
            #add game to list
            games.append(game_id)
            game_total += 1

#print unique team list
print("Total Teams:", team_total)
#print unique player list
print("Total PLayers:", player_total)
#print total games
print(f"Total Games: {game_total}")

#print(player_dir)
