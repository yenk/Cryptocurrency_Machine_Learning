import json 
import requests 
import quandl 

# quandl.ApiConfig.api_key = 'PqkvcuuERzoHuu3D9Avz'
quandl.ApiConfig.api_key = 'PqkvcuuERzoHuu3D9Avz'

##############################
# Making json api call to get full dataset 
##############################

# url = 'https://www.quandl.com/api/v3/datasets/GDAX/USD.json'
url = 'https://www.quandl.com/api/v3/datasets/GDAX/GBP.json'


def api_call(url): 
  data = requests.get(url) #returns a response object
  data.raise_for_status() #check for errors
  BTCdata = json.loads(data.text) 
  return BTCdata

BTCdata = api_call(url)

#writing to a json file 
with open('btcdata.json','w') as outfile: 
  json.dump(BTCdata, outfile) 


