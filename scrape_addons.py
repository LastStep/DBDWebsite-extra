import requests
from bs4 import BeautifulSoup as bs
from collections import defaultdict
import json, re

data = defaultdict()
url = 'https://deadbydaylight.gamepedia.com/Add-ons'

killer_num = 4

site = bs(requests.get(url).content, 'lxml')

table = site.find('div', {'class': 'mw-parser-output'})
table = table.find_all('table', {'class':'wikitable'})[killer_num]
table = table.find('tbody')

name = site.find_all('div', {'class':'floatleft'})[killer_num-1]
power = site.find_all('div', {'class':'floatright'})[killer_num]

temp = defaultdict()
nth = name.a
killer = nth['title']
pth = power.a
temp['power'] = pth['title']
temp['killer-image'] = nth.img['src']
temp['killer-image-alt'] = "/static/images/Killer_Portraits/***_charSelect_portrait.png"
temp['power-image'] = pth.img['src']
temp['power-image-alt'] = "/static/images/Powers/iconPowers_***.png"
temp['power-description'] = "Yamaoka's Wrath is The Oni's main Power: it allows him to go into a Blood Fury by absorbing Blood Orbs dropped by injured survivors. When he is in this Blood Fury, he can dash at high speeds and deal a horrible blow to the survivor's with his Kanabō, which downs them in a single hit."
temp['addons'] = defaultdict(list)

for tr in table.contents[1:]:
    try:
        text = tr.text
    except:
        continue
	
    
    tempp = defaultdict()
    th = tr.find_all('th')
    td = tr.find_all('td')
    tempp['addon-image'] = th[0].img['src']
    tempp['addon-name'] = th[1].text.strip()
    addon_rarity = td[0].text.strip()
    tempp['addon-description'] = td[1].text.strip()
    tempp['addon-image-alt'] = "/static/images/Addons/iconAddon_***.png"
    tempp['addon-id'] = '{}-{}'.format(re.sub(r"[^a-zA-Z0-9]+", '-', tempp['addon-name'].replace(' ', '-')), killer)
    tempp['addon-effect'] = '***'
    temp['addons'][addon_rarity].append(tempp)

data[killer] = temp

ddd = {}
keys = sorted(data.keys())
for key in keys:
    ddd[key] = data[key]

with open(r"Killer_Addons.json", "w") as f:
    json.dump(ddd, f)
