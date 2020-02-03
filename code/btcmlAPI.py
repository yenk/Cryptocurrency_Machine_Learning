import json 
import requests 
import quandl 

quandl.ApiConfig.api_key = 'PqkvcuuERzoHuu3D9Avz'

##############################
# Making json api call to get full dataset 
##############################

url = 'https://www.quandl.com/api/v3/datasets/GDAX/GBP.json'

def function(__self__):
	class ClassName(object):
		def __init__(self, arg):
			super(ClassName, self).__init__()
			self.arg = arg		
	pass

def api_call(url): 
	# returns a response object
	data = requests.get(url) 
	# check for errors
	data.raise_for_status() 
	BTCdata = json.loads(data.text) 
	return BTCdata

BTCdata = api_call(url)

# writing to a json file 
with open('btcdata.json','w') as outfile: 
  json.dump(BTCdata, outfile) 


