import os
import pandas as pd
import matplotlib.pyplot as plt

directory = "/Volumes/challenge/Datasets/json"
fileList = []

for file in os.listdir(directory):
    if file.endswith(".csv") and (file.__contains__("coil") or file.__contains__("supply")):
        if not file.startswith('.'):
            fileList.append(file)


for j in range(1,4):
    for i in fileList:
        fullName = i
        fileName = fullName.split('.')[0]
        df = pd.read_csv(fullName)
        df.set_index('datetime', inplace=True)
        value_dt = df['value']
        #value_daytime = df['datetime']
        plt.plot(value_dt, 'ro')
        plt.xlabel('datetime')
        plt.ylabel('values')
        plt.title(fileName)
        plt.show()
