from datetime import datetime, timedelta
from get_nasa_objects import get_near_earth_objects
from filter_data import filter_data
from sort_by_magnitude import reverse_sort_by_magnitude

# import os for getting key from environment variables


# print('Use date format YYYY-MM-DD')
# print('Input start date')
# start_date = input()
# print('Input end date')
# end_date = input()
# print("How many the nearest objects must be printed per date?")
# top_num = input()
# api_key = os.environ['APIKEY']
key_list = ['name', 'absolute_magnitude_h', 'is_potentially_hazardous_asteroid']
key_list.append('neo_reference_id')
# SAMPLE DATA
start_date = '2015-09-07'
end_date = '2015-09-10'

date_format = '%Y-%m-%d'
start_date_time = datetime.strptime(start_date, date_format)
end_date_time = datetime.strptime('2015-09-10', date_format)
days = [(start_date_time + timedelta(days=day)).strftime(date_format) for day in
        range((end_date_time - start_date_time).days + 1)]
top_num = 3

objects = get_near_earth_objects(str(start_date_time), str(end_date_time), api_key)
filtered_objects_by_date = filter_data(objects, key_list)

for day in days:
    print('\n' + day)
    sorted_list = reverse_sort_by_magnitude(filtered_objects_by_date[day])
    if len(sorted_list) < top_num:
        print(f"\033[93mTop num exceeds amount of objects per day, listing all values per day\033[0m")
    for obj in sorted_list[0:top_num]:
        sorted_map = [obj[key] for key in key_list[0:-1]]
        print(f"{obj['neo_reference_id']}: {sorted_map}")
