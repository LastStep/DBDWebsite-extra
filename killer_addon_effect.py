import json
from collections import defaultdict


with open(r'E:\Python Projects\Flask Apps\Killer_Addons.json', 'r') as f:
	killer_addons = json.load(f)

with open(r'E:\Python Projects\Flask Apps\Hillbilly.json', 'r') as f:
	hillbilly = json.load(f)

killer_name = 'Hillbilly'
addons_dict = defaultdict()
for key1, item1 in hillbilly.items():
	main_stats = key1
	for key2, item2 in item1.items():
		if item2 != None and key2 != f'Base-{killer_name}':
			if key1 == 'Additional Effects':
				item_effect = item2
			else:
				item_effect = key1 + ': ' + item2
			if key2 in addons_dict:
				addons_dict[key2] += '\\n\\n' + item_effect
			else:
				addons_dict[key2] = item_effect

# print(addons_dict)
for killer, info in killer_addons.items():
	if killer == killer_name:
		for rarity, addons in info['addons'].items():
			for addon in addons:
				for key, item in addons_dict.items():
					if key == addon['addon-id']:
						addon['addon-effect'] = item

with open(r'E:\Python Projects\Flask Apps\Killer_Addons.json', 'w') as f:
	json.dump(killer_addons, f)