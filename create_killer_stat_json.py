import pandas as pd
import json

killers = ['Doctor']

for killer in killers:
	killer_stats = pd.read_csv(r'C:\Users\Gray\Random\DBDWebsite\app\static\files\{}.csv'.format(killer), index_col=0)

	killer_stats.to_json(r'C:\Users\Gray\Random\DBDWebsite\app\static\files\Killer_Addons\{}.json'.format(killer))