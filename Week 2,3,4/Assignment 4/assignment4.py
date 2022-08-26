import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Precipitation data
precdf = pd.read_csv('D:/Data Science/Applied Plotting, Charting & Data Representation in Python/Week 2,3,4/Assignment 4/Precipitation.csv')
precdf.drop(index=[0,7,8,9,10,11,12],inplace=True)

new_header = precdf.iloc[0]
precdf = precdf[1:]
precdf.columns = new_header
precdf.drop(["Annual"],axis=1,inplace=True)
precdf.columns.name = None
precdf.set_index("Year",inplace=True)

prec2017 = precdf.iloc[0].squeeze()
prec2017 = prec2017.add_suffix(" 2017")
prec2018 = precdf.iloc[1].squeeze()
prec2018 = prec2018.add_suffix(" 2018")
prec2019 = precdf.iloc[2].squeeze()
prec2019 = prec2019.add_suffix(" 2019")
prec2020 = precdf.iloc[3].squeeze()
prec2020 = prec2020.add_suffix(" 2020")
prec2021 = precdf.iloc[4].squeeze()
prec2021 = prec2021.add_suffix(" 2021")
prec = pd.concat((prec2017,prec2018,prec2019,prec2020,prec2021))
prec = prec.astype(float)

# Temperature data
tempdf = pd.read_csv('D:/Data Science/Applied Plotting, Charting & Data Representation in Python/Week 2,3,4/Assignment 4/Temperature.csv')
tempdf.drop(index=[0,7,8,9,10,11,12,13,14],inplace=True)

new_header = tempdf.iloc[0]
tempdf = tempdf[1:]
tempdf.columns = new_header
tempdf.drop(["Annual"],axis=1,inplace=True)
tempdf.columns.name = None
tempdf.set_index("Year",inplace=True)
print(tempdf)

temp2017 = tempdf.iloc[0].squeeze()
temp2017 = temp2017.add_suffix(" 2017")
temp2018 = tempdf.iloc[1].squeeze()
temp2018 = temp2018.add_suffix(" 2018")
temp2019 = tempdf.iloc[2].squeeze()
temp2019 = temp2019.add_suffix(" 2019")
temp2020 = tempdf.iloc[3].squeeze()
temp2020 = temp2020.add_suffix(" 2020")
temp2021 = tempdf.iloc[4].squeeze()
temp2021 = temp2021.add_suffix(" 2021")
temp = pd.concat((temp2017,temp2018,temp2019,temp2020,temp2021))
temp.drop(labels=["Mar 2018", "Nov 2019", "Apr 2021"], inplace=True)
print(temp)
temp = temp.astype(float)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.plot(prec.index, prec, 'g-')
ax2.plot(temp.index, temp, 'b-')
plt.show()
