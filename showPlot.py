import matplotlib.pyplot as plt
import pandas as pd

new_file = pd.read_csv('outfile.csv')
#new_file.set_index('datetime', inplace=True)

data = new_file[['Humidity value', 'datetime']]
print(data)
#data.set_index('datetime', inplace=True)
data.plot()
plt.xticks(rotation=45)
plt.xlabel('Datetime')
plt.ylabel('Humidity value')
plt.title('Humidity')
plt.show()
