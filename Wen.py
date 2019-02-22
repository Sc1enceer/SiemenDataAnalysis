import pandas as pd
import matplotlib.pyplot as plt

Mote_704 = pd.read_csv("Mote 704 from 25-04-2017 15-05-01 to 02-05-2017 15-05-01.csv")

Mote_704['Timestamp'] = pd.to_datetime(Mote_704['Timestamp'], format='%d/%m/%Y %H:%M:%S')

Mote_704.sort_values('Timestamp', inplace = True, ascending = True)
Mote_704.set_index('Timestamp', inplace=True)

time_car = Mote_704[ "Carbon Monoxide"]



plt.plot(time_car)
plt.xticks(rotation=45)
plt.xlabel('Timestamp')
plt.ylabel('Carbon Monoxide')
plt.title('sample')




plt.show()