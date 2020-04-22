import requests
from bs4 import BeautifulSoup as bs
from collections import defaultdict
import json
data = defaultdict()
url = 'https://deadbydaylight.gamepedia.com/Items'
site = bs(requests.get(url).content, 'lxml')
table = site.find('div', {'class': 'mw-parser-output'})
table = table.find_all('table', {'class':lambda x: x and 'sortable' in x and 'unsortable' not in x})[-1]
table = table.find('tbody')