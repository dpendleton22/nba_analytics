#This provides a intro "how to" with the nba_py library 
import requests
import csv
import nba_py
from nba_py import team
from nba_py import player
import pandas as pd
import datetime as dt
import matplotlib.pyplot as pt

if __name__ == '__main__':
    date = dt.date.today()
    #Get the summary information on the Cleveland Cavaliers 
    team_id = nba_py.constants.TEAMS.get('CLE').get('id')
    cle_team = nba_py.team.TeamSummary(team_id=team_id)
    lebronJames = nba_py.player.get_player('lebron', 'james')
    test = nba_py.Scoreboard(date.month, date.day - 1, date.year)
    nba_df = pd.DataFrame(test.line_score())
    list_a = []
    list_b = []
    list_c = []
    for x in range(len(nba_df.index)):
        if x%2 == 0:
            list_c.append(nba_df.loc[x, 'GAME_SEQUENCE'])
            list_a.append(nba_df.loc[x, 'PTS'])
        else:
            list_b.append(nba_df.loc[x, 'PTS'])
    print("List_c: %s" % list_c)
    print ("List a: %s" % list_a)
    print ("List_b: %s" % list_b)
    pt.bar(list_c, list_a,  color='r', width=0.4)
    list_d = [x+0.4 for x in list_c]
    pt.bar(list_d, list_b, color='b', width=0.4)
    print (list_d)
    # grouped = nba_df.groupby('GAME_SEQUENCE')
    # print (grouped.get_group(1)['PTS'])
    # ax = grouped.plot.bar(x='TEAM_ABBREVIATION', y='PTS')
    # for i, v in enumerate(grouped['PTS']):
    #     ax.text(v + 3, i + .25, str(v), color='blue', fontweight='bold')
    # for x in nba_df['GAME_SEQUENCE']:
    #     print (x)
    #     ax.bar(grouped.get_group(x)['TEAM_ID'], grouped.get_group(x)['PTS'], align = 'center', width=1.0)
        # ax.xticks(grouped.get_group(x)['TEAM_ID'], grouped.get_group(x)['TEAM_ABBREVIATION'])
    pt.show()
