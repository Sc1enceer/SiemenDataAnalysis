
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





first = fileList[3]
print(first)
df = pd.read_csv(first)
value_dt = df[['datetime', 'value']]
value_dt.reindex()
fileName = first.split('.')[0]
list = []
n = len(value_dt.datetime)
for i in range(n):
    date = value_dt.loc[i].datetime.split(' ')[1].split(':')[0]
    list.append(date)



df["hour"] = list
#value_dt.sort_values("datetime", inplace=True)

#df["hour"] = value_dt["hour"]
df.sort_values("datetime", inplace=True)
df.to_csv("hum_sensor_hum.csv")

meanForEachHour = np.round(df.pivot_table(index="hour", values="value", aggfunc=np.mean), 2)

'''
n = len(meanForEachHour)
averageList = []
for i in range(n):
    value = meanForEachHour[i][0]
    averageList.append(value)
'''

print(meanForEachHour)





#plot the data

for i in fileList:
    fullName = i
    fileName = fullName.split('.')[0]
    df = pd.read_csv(fullName)
    df.set_index('datetime', inplace=True)
    value_dt = df['value']
    print(value_dt.head())
    value_dt.plot()
    plt.xlabel('datetime')
    plt.ylabel('values')
    plt.title(fileName)
    plt.show()


