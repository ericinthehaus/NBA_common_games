import pandas as pd
import os
import functions 
import numpy as np

games = pd.read_csv("./games2024.csv", parse_dates=[0])
# let's only use games in the Regular Season 
games = games[games['HomeWin'].notnull()].reindex()
games['Winner'] = np.where(games['HomeWin'] == True, games['Home'], games['Visitor'])
games['Loser'] = np.where(games['HomeWin'] == True, games['Visitor'], games['Home'])
print(games)

teamA = "IND"
teamB = "MIL"
functions.common_games(games, teamA, teamB)

functions.common_games_decision(games, teamA, teamB)

all_teams = pd.unique(games['Winner'])
functions.season_leaders(all_teams, games) 