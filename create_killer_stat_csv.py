import pandas as pd
import json

killer_name = 'Doctor'
input_rows = ['Shock Range','Static Blast Cooldown','Shock Therapy Detonation Delay','Terror Radius (SB on Cooldown)','Terror Radius (SB off Cooldown)']


with open(r'C:\Users\Gray\Random\DBDWebsite\app\static\files\Killer_Addons.json', 'r') as f:
    killer_addons = json.load(f)

dataframe_rows = ['']
for i in input_rows:
    dataframe_rows.append(i)
dataframe_rows.append('Additional Effects')

dataframe_columns = [f'Base-{killer_name}', f'Static-{killer_name}']
for killer, info in killer_addons.items():
    if killer == killer_name:
        for rarity, addons in info['addons'].items():
            for addon in addons:
                dataframe_columns.append(addon['addon-id'])

df = pd.DataFrame(columns=dataframe_rows)
df[''] = dataframe_columns

df.to_csv(r'C:\Users\Gray\Random\DBDWebsite\app\static\files\{}.csv'.format(killer_name), index=False)
