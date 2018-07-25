#This provides a intro "how to" with the nba_py library 
import requests
import csv
import nba_py
from nba_py import team
from nba_py import player
import pandas as pd
import datetime as dt
import matplotlib.pyplot as pt

'''
get_Team_Summary
Provides a summary/history of the desired team

input
-----
team_abbriv: String
    Abbreviation of the team to get a summary of. 
    Example: Cleveland Cavaliers = 'CLE'
             Golden State Warriors = 'GSW'

return
------
team_info: Dataframe 
    Includes Team ID, Season Year, Team City, Team Conference
    Team Division, Wins, Losses, Conf Rank, Division Rank, Origin Year
'''
def get_team_summary(team_abbriv = 'CLE'):
    team_id = nba_py.constants.TEAMS.get(team_abbriv).get('id')
    team_summary = nba_py.team.TeamSummary(team_id=team_id)
    team_info = team_summary.info()
    return team_info

'''
get_player_stats
Provides the desired player up-to-date headline stats (PTS, AST, REB, PIE)

input
-----
player_name: String
    Name of player to get stats

return
------
get_player_summary: Dataframe
    returns the headline stats of the player 
'''
def get_player_stats(player_name= 'lebron james'):
    first, last = player_name.split()
    get_player_id = nba_py.player.get_player(first, last, just_id=True)
    get_player_summary = nba_py.player.PlayerSummary(get_player_id).headline_stats()
    return get_player_summary

'''
get_player_stats_vs_opponent
    Provides the desired player stats vs a specific opponent

input
-----
player_name: String 
    Name of player to get stats 

opp_team: String
    Name of the opponent team to compare with player stats

all_opponents: Boolean
    get player stats vs all NBA opponents

return
------
get_player_vs_opponent: Dataframe
    returns the player stats including (wins, loses, minutes, field goal pct)
'''
def get_player_stats_vs_opponent(player_name='lebron james', opponent_name='Boston Celtics', all_opponents=False):
    first, last = player_name.split()
    player_id = nba_py.player.get_player(first, last, just_id=True)
    player_dash = nba_py.player._PlayerDashboard(player_id)
    play_split = nba_py.player.PlayerOpponentSplits(player_id)
    return play_split.by_opponent()

'''
get_player_shooting_stats
    Provides shot area details for the specified player

input
-----
player_name: String 
    Name of player to get stats 

return
------
player_shooting_stats: Dataframe
    returns player shooting area stats from various areas on the court
'''
def get_player_shooting_stats(player_name='lebron james'):
    first, last = player_name.split()
    player_id = nba_py.player.get_player(first, last, just_id=True)
    player_dash = nba_py.player._PlayerDashboard(player_id)
    player_split = nba_py.player.PlayerShootingSplits(player_id)
    return player_split.overall()

'''
nba_scoreboard
    Provides nba games scores from the past night

input
-----
    None

return
------
nba_scoreboard: Dataframe
    Provides the nba scores fromt the past week
'''
def nba_scoreboard():
    date = dt.date.today()
    yesterdays_score = nba_py.Scoreboard(date.month, date.day - 1, date.year)
    nba_scores = pd.DataFrame(yesterdays_score.line_score())
    return nba_scores

