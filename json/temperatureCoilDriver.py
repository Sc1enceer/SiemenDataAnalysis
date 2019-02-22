import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

directory = "/Volumes/challenge/Datasets/json"

# append all file names in the directory into the list
fileList = []
for file in os.listdir(directory):
    if file.endswith(".csv"):
        if not file.startswith('.'):
            fileList.append(file)

print(fileList)
heat_coil_driver = fileList[1]
supply_temp = fileList[5]

df = pd.read_csv(supply_temp)
value_dt = df[['datetime', 'value']]

fileName = heat_coil_driver.split('.')[0]
list = []
n = len(value_dt.datetime)
for i in range(n):
    date = value_dt.loc[i].datetime.split(' ')[1].split(':')[0]
    list.append(date)


df.sort_values("datetime", inplace=True)

list = []

for i in range(1,24):
    list.append(np.std(df.loc[i:i+12]['value']))
maxVal = np.max(list)
position = -1
for i in range(1,24):
    if list[i] == maxVal:
        position = i
        break

values = df.loc[position*12:(position+1)*12]['value']


df2 = pd.read_csv(heat_coil_driver)
heat_coil_driver = df2.loc[position*12:(position+1)*12]['value']

print(values)
print("••••••••••••••••••••••••••••••••••")
print(heat_coil_driver)
