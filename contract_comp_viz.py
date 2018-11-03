"""Summary

Attributes:
    contract_ranking (list): Description
    df (TYPE): Description
    per_cols (list): Description
    salary_cols (list): Description
    standardize (TYPE): Description
"""
import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.offline as pltly
import plotly.graph_objs as go
from data import SALARY_DATA, PER_DATA, BPM_DATA, TM_DATA



"""
Resources:
https://www.basketball-reference.com/contracts/players.html
https://www.reddit.com/r/nba/comments/6dvmr1/best_advanced_stat_to_measure_how_good_a_player_is/
https://fansided.com/2017/01/31/nylon-calculus-reinventing-per/

Looks like best all in one stats are
PER (Player Efficiency Rating)
WS (Win Shares)
RPM (Real Plus Minus)
BPM (Boxscore Plus Minus)
"""

# get rid of the stuff to the right of \ i.e. LeBron James\jamesle01
standardize = lambda f:f.rsplit('\\')[0].lower()
# make money a float not a string
def monify(m):
	"""Summary
	
	Args:
	    m (string): money string
	
	Returns:
	    float: money value
	"""
	try:
		return float(re.sub('[$,]', '', m))
	except:
		return m

SALARY_DATA['Player'] = SALARY_DATA['Player'].map(standardize)
SALARY_DATA['Guaranteed'] = SALARY_DATA['Guaranteed'].map(monify)
PER_DATA['Player'] = PER_DATA['Player'].map(standardize)
#Make sure you only include players that have played at least 30 minutes in the season
PER_DATA = PER_DATA.loc[PER_DATA.MP > 30]
#The BPM is included in the new player PER data added 2017_2018_PER_regszn
# BPM_DATA['Player'] = BPM_DATA['Player'].map(standardize)
TM_DATA['Win Percentage'] = TM_DATA['W']/82.

salary_cols = ['Player','Tm','Signed Using','Guaranteed']
per_cols = ['Rank','Player','PER', 'BPM']
#The BPM is included in the new player PER data added 2017_2018_PER_regszn
# bpm_cols = ['Player','BPM']
tm_cols = ['Tm','Win Percentage']

df = TM_DATA[tm_cols].merge(SALARY_DATA[salary_cols].merge(PER_DATA[per_cols], on='Player'), on='Tm')
#Drop duplicates of players with multiple PER's for the same team
df. drop_duplicates(subset=['Player','Tm'], inplace = True)

print df

"""
Visualization
"""

sns.set(style="whitegrid")
f, ax = plt.subplots(figsize=(6.5, 6.5))


contract_ranking = ["Early Bird", "Cap space", "1st Round Pick", "Non-Bird rights", "MLE", "Bi-annual Exception", "Minimum Salary"]
sns.scatterplot(x="PER", y="Guaranteed",
                hue="Tm",
                # hue_order=contract_ranking,
                sizes=(1, 8), linewidth=0,
                data=df, ax=ax)

ax.get_yaxis().get_major_formatter().set_scientific(False)
plt.suptitle("Player Efficiency vs. Guaranteed $\$ by Team")

# plt.show()

tracePER = go.Scatter(x=df['PER'],y=df['Guaranteed'],mode='markers',name='PER',
	text=df['Player'],
	marker=dict(
        size=16,
        color = df['Win Percentage'], #set color equal to a variable
        colorbar=dict(title='Team Win Percentage (%)'),
        colorscale='Viridis',
        showscale=True
    ))
traceBPM = go.Scatter(x=df['BPM'],y=df['Guaranteed'],mode='markers',name='BPM',
		text=df['Player'],
	marker=dict(
        size=16,
        color = df['Win Percentage'], #set color equal to a variable
        colorbar=dict(title='Team Win Percentage (%)'),
        colorscale='Viridis',
        showscale=True
    ))


layout = go.Layout(
    title='Good Contract, Bad Contract',
    xaxis=dict(
        title='Player Efficiency Rating (PER)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Contract Guarantee ($)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=[tracePER], layout=layout)


# data = [tracePER]

pltly.plot(fig)

# pltly.plot([traceBPM])




