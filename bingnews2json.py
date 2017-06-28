import requests as rq
from pymongo import MongoClient

url = 'https://api.cognitive.microsoft.com/bing/v5.0/news/search?q=&mkt=de-de'
headers = {'Authorization': apikey, 'Content-Type' : 'application/json'}
r = rq.get(url, data=dumps(item), headers=headers)