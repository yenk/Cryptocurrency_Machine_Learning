import btcmlMain as bm 

#########
# calling class 
#########
final_data_manip_list = bm.DataWrangle()
datawrangle = bm.DataWrangle()
by_day_all_values = datawrangle.get_all_day_values(datetime(2018,1,20))
by_year_range = datawrangle.get_year_range()
month_lookup = datawrangle.month_dict_lookup()
day_lookup = datawrangle.day_dict_lookup()
by_month_values = datawrangle.get_month_values('High')

print(by_month_values)
print(monthly_lookup)
print(day_value)
print(by_day_all_values)
print(all_year_lookup)
print(by_year_range)