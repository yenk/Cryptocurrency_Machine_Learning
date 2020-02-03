import btcmlAPI 
import dateutil.parser as parser 
import json 

############################## 
# This module extracts and transforms 
# json dataset. 
##############################

#Load json file 
BTCdata_load = json.loads(open('BTCdata.json').read())

def transformed_load_data(BTCdata_load): 
  BTCdata_list = []

  for row in BTCdata_load['dataset']['data']:
    date=row[0]
    open=row[1]
    high=row[2]
    low=row[3]
    volume=row[4]
    BTC_dict = dict({'Date':date,'Open':open,'High':high,'Low':low,'Volume':volume})
    BTCdata_list.append(BTC_dict)
  return BTCdata_list

##########
# date parsing into a list of dictionaries 
##########
BTCdata_list = transformed_load_data(BTCdata_load)

def price_by_date(BTCdata_list):
  final_data_manip_list = [] 
  for price_dict in BTCdata_list:
    # parsing date to new dictionary 
    new_price_dict = {}
    new_price_dict['Date'] = parser.parse(price_dict['Date'])
    # new_price_dict['Date'] = parser.parse(price_dict(date).year)
    new_price_dict['Open'] = price_dict['Open']
    new_price_dict['High'] = price_dict['High']
    new_price_dict['Low'] = price_dict['Low']
    new_price_dict['Volume'] = price_dict['Volume']
    final_data_manip_list.append(new_price_dict)
  return final_data_manip_list
