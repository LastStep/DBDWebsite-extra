import pandas as pd
import json

item_name = 'Key'
input_rows = ['Durability']


with open(r'C:\Users\Gray\Random\DBDWebsite\app\static\files\Items.json', 'r') as f:
    item_addons = json.load(f)

dataframe_rows = ['']
for i in input_rows:
    dataframe_rows.append(i)
dataframe_rows.append('Additional Effects')

dataframe_columns = [f'Base-{item_name}', f'Static-{item_name}']
for addons in item_addons[item_name]['addons'].values():
	for addon in addons:
		addon_id = ''.join([i if i != ' ' else '-' for i in addon['addon-name']])
		dataframe_columns.append(addon_id)

df = pd.DataFrame(columns=dataframe_rows)
df[''] = dataframe_columns

df.to_csv(r'C:\Users\Gray\Random\DBDWebsite\app\static\files\Item_Addons\{}.csv'.format(item_name), index=False)
