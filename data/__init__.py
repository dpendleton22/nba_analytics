import os
import pandas as pd

SALARY_DATA = pd.read_csv(os.path.join(os.path.dirname(__file__),'salary_contract_player.csv'))
PER_DATA = pd.read_csv(os.path.join(os.path.dirname(__file__),'PER_player_career_regszn.csv'))
BPM_DATA = pd.read_csv(os.path.join(os.path.dirname(__file__),'BPM_player_career_regszn.csv'))
TM_DATA = pd.read_csv(os.path.join(os.path.dirname(__file__),'team_data.csv'))