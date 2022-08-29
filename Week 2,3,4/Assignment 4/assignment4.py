import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import numpy as np

# Precipitation data
precdf = pd.read_csv('D:/Data Science/Applied Plotting, Charting & Data Representation in Python/Week 2,3,4/Assignment 4/Precipitation.csv')
precdf.drop(index=[0,2,3,4,7,8,9,10,11,12],inplace=True)

new_header = precdf.iloc[0]
precdf = precdf[1:]
precdf.columns = new_header
precdf.drop(["Annual"],axis=1,inplace=True)
precdf.columns.name = None
precdf.set_index("Year",inplace=True)

prec2020 = precdf.iloc[0].squeeze()
prec2020 = prec2020.add_suffix(" 2020")
prec2021 = precdf.iloc[1].squeeze()
prec2021 = prec2021.add_suffix(" 2021")
prec = pd.concat((prec2020,prec2021))
prec = prec.astype(float)

# Temperature data
tempdf = pd.read_csv('D:/Data Science/Applied Plotting, Charting & Data Representation in Python/Week 2,3,4/Assignment 4/Temperature.csv')
tempdf.drop(index=[0,2,3,4,7,8,9,10,11,12,13,14],inplace=True)

new_header = tempdf.iloc[0]
tempdf = tempdf[1:]
tempdf.columns = new_header
tempdf.drop(["Annual"],axis=1,inplace=True)
tempdf.columns.name = None
tempdf.set_index("Year",inplace=True)

temp2020 = tempdf.iloc[0].squeeze()
temp2020 = temp2020.add_suffix(" 2020")
temp2021 = tempdf.iloc[1].squeeze()
temp2021 = temp2021.add_suffix(" 2021")
temp = pd.concat((temp2020,temp2021))
temp.drop(labels=["Apr 2021"], inplace=True)
temp = temp.astype(float)

# Visual

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
lns1 = ax1.plot(prec.index, prec, '#0072B2', label="Precipitation Monthly Totals")
lns2 = ax2.plot(temp.index, temp, '#D55E00', label="Temperature Monthly Totals")
ax1.set_xlabel("Month")
ax1.set_ylabel("Precipitation (inches)")
ax2.set_ylabel("Temperature (F°)")
ax1.set_title("Precipitation and Temperature Monthly Totals in\nAnn Arbor, MI, United States (2020-2021)")
lns = lns1+lns2
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=9)
ax1.set_xticks(np.arange(1, len(prec.index)+1, 2))
fig.autofmt_xdate(rotation=45)

prec.drop(labels=["Apr 2021"], inplace=True)
corr, pval = stats.pearsonr(prec, temp)
print(corr)

plt.show()

