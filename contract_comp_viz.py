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
from data import SALARY_DATA, PER_DATA, BPM_DATA



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
BPM_DATA['Player'] = BPM_DATA['Player'].map(standardize)



salary_cols = ['Player','Tm','Signed Using','Guaranteed']
per_cols = ['Rank','Player','PER']
bpm_cols = ['Player','BPM']

df = SALARY_DATA[salary_cols].merge(PER_DATA[per_cols], on='Player').merge(BPM_DATA[bpm_cols], on='Player')

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

plt.show()

tracePER = go.Scatter(x=df['PER'],y=df['Guaranteed'],mode='markers',name='PER')
traceBPM = go.Scatter(x=df['BPM'],y=df['Guaranteed'],mode='markers',name='BPM')


data = [tracePER]

pltly.plot(data)

pltly.plot([traceBPM])




