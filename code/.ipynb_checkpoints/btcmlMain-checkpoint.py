import btcmlLoad as bl 
import json 
from datetime import datetime, timedelta, date 

##############################
# This class module is implemented 
# to develop analytics and plots 
##############################
BTCdata_load = json.loads(open('BTCdata.json').read())
BTCdata_list = bl.transformed_load_data(BTCdata_load)
final_data_manip_list = bl.price_by_date(BTCdata_list)

class DataWrangle: 

  def __init__(self, final_data_manip_list):

    self.final_data_manip_list=final_data_manip_list
    self.date_lookup_dict = {}
    self.__create_day_lookup() 
    self.__create_month_lookup() 

  def __create_day_lookup(self): 
    """
    Create a date lookup to extract every record
    """
    keys = ['Open', 'High', 'Low', 'Volume']
    self.date_lookup_dict = {price_dict['Date']:{k:price_dict[k] for k in keys} for price_dict in self.final_data_manip_list} #builds raw daily data

  def __create_month_lookup(self): 
    """
    Create a monthly lookup to extract data by month 
    """
    # month_rename = {12:'Dec',11:'Nov',10:'Oct',9:'Sep',8:'Aug',7:'Jul',6:'Jun',5:'May',4:'Apr',3:'Mar',2:'Feb',1:'Jan'}
    self.monthly_lookup = {x:[] for x in range(1,13)}
    for item in self.final_data_manip_list: 
      self.monthly_lookup[item['Date'].month].append(item)

  def get_all_day_values(self, requested_date):
    for items in self.date_lookup_dict: 
      if requested_date in self.date_lookup_dict:
        return self.date_lookup_dict[requested_date]

  def get_month_values(self, requested_value): 
    self.month_by_values_dict = {k:v for k, v in self.monthly_lookup.items() if requested_value in self.monthly_lookup}
      # if requested_value in self.monthly_lookup
    return self.month_by_values_dict

  def get_year_aggregates(self): 
    """
    Creates an aggregated yearly output 
    """
    keys = ['Open', 'High', 'Low', 'Volume']
    self.year_dict = {price_dict['Date']:{k:price_dict[k] for k in keys} for price_dict in self.date_lookup_dict} #{2016, 2017, 2018, 2014, 2015}
    # for item in self.year_dict: 
    #   if requested_year in self.year_dict: 
  #   keys = [k for k in self.date_lookup_dict [k.strftime('%Y')]]
  #   return keys 
    # self.year_key = {k:v for k, v in self.date_lookup_dict.items()}
    # return self.year_key
    # self.year_key = {k:v for k, v in self.date_lookup_dict}
    return self.year_dict 
    # if requested_year in self.year_key:
      # return self.year_key[requested_year]
    # self.year_key_list = {k for k in self.year_key.items()}
    # for key, value in self.year_key: 
      # return key.strftime('%Y'), value #('2018', {'Open': 1518.0, 'High': 1555.0, 'Low': 1256.0, 'Volume': 16715.54305141})

  def day_dict_lookup(self):
    return self.date_lookup_dict #returns raw data 

  def month_dict_lookup(self): 
    return self.monthly_lookup
    

##########
# calling class 
##########
datawrangle = DataWrangle(final_data_manip_list)
by_day_all_values = datawrangle.get_all_day_values(datetime(2018,1,20))
# by_year_range = datawrangle.get_year_range()
by_year_aggregates = datawrangle.get_year_aggregates()
month_lookup = datawrangle.month_dict_lookup()
day_lookup = datawrangle.day_dict_lookup()
by_month_values = datawrangle.get_month_values('High')

# print(by_month_values)
# print(month_lookup)
# print(by_day_all_values)
# print(day_lookup)
print(by_year_aggregates)

