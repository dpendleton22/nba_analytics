import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data import SALARY_DATA, PER_DATA



"""
Resources:
https://www.basketball-reference.com/contracts/players.html
https://www.reddit.com/r/nba/comments/6dvmr1/best_advanced_stat_to_measure_how_good_a_player_is/
https://fansided.com/2017/01/31/nylon-calculus-reinventing-per/

Looks like best all in one stats are
PER (Player Efficiency Rating)
WS (Win Shares)
RPM (Real Plus Minus)
BPM (?)
"""

# get rid of the stuff to the right of \ i.e. LeBron James\jamesle01
standardize = lambda f:f.rsplit('\\')[0].lower()
# make money a float not a string
def monify(m):
	try:
		return float(m.split('$')[1])
	except:
		return m

SALARY_DATA['Player'] = SALARY_DATA['Player'].map(standardize)
SALARY_DATA['Guaranteed'] = SALARY_DATA['Guaranteed'].map(monify)
PER_DATA['Player'] = PER_DATA['Player'].map(standardize)



salary_cols = ['Player','Tm','Signed Using','Guaranteed']
per_cols = ['Rank','Player','PER']

df = SALARY_DATA[salary_cols].merge(PER_DATA[per_cols], on='Player')

"""
Visualization
"""

sns.set(style="whitegrid")
f, ax = plt.subplots(figsize=(6.5, 6.5))

contract_ranking = ["Early Bird", "Cap space", "1st Round Pick", "Non-Bird rights", "MLE", "Bi-annual Exception", "Minimum Salary"]
sns.scatterplot(x="PER", y="Guaranteed",
                hue="Signed Using",
                # hue_order=contract_ranking,
                sizes=(1, 8), linewidth=0,
                data=df, ax=ax)

plt.show()

