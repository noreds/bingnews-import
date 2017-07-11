import requests as rq
from pymongo import MongoClient
import time
import json
import os

source = 'Microsoft'
apikey = 'badb775479d94c869170ee6fc860433f'
url = 'https://api.cognitive.microsoft.com/bing/v7.0/news?mkt=de-de'
headers = {'Ocp-Apim-Subscription-Key': apikey, 'Content-Type' : 'application/json'}
r = rq.get(url, headers=headers)
imported_news = 'imported'
if not os.path.isdir(imported_news):
    os.mkdir(imported_news)
filename = '%s_%s.json' % (source, time.time())
with open(os.path.join(imported_news, filename), 'w+', encoding='utf8') as f:
    json.dump(r.json(), f, ensure_ascii=False)
