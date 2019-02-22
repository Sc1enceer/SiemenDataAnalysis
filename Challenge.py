import json
import csv
import pandas as pd


with open('AHU06 Supply Temp.json', 'r') as f:
    entireFile = json.load(f)

n = len(entireFile['values'])


with open('supply_temp.csv', 'w') as output_file:

    data_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['datetime', 'time', 'temp value'])

    for i in range(n):
        data = ""
        value = str(entireFile['values'][i]['value'])
        time = str(entireFile['values'][i]['time'])
        datetime = str(entireFile['values'][i]['datetime']).replace('T', " ").replace('Z', "")
        data_writer.writerow([datetime, time, value])


new_file = pd.read_csv('supply_temp.csv')
new_file['datetime'] = pd.to_datetime(new_file['datetime'], format='%Y/%m/%d %H:%M:%S')
new_file.sort_values('datetime', inplace=True, ascending=True)
new_file.set_index('datetime', inplace=True)






