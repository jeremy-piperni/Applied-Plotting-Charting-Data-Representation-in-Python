import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import numpy as np


datadf = pd.read_csv('D:/Data Science/Applied Plotting, Charting & Data Representation in Python/Week 2,3,4/data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

datadf["Data_Value"] = datadf["Data_Value"] / 10
datadf["Date"] = pd.to_datetime(datadf["Date"])
datadf = datadf.drop(datadf[(datadf["Date"].dt.day == 29) & (datadf["Date"].dt.month == 2)].index)

mindata = datadf[datadf["Element"]=="TMIN"]
mindata2015 = mindata[mindata["Date"].dt.year == 2015]
mindata = mindata.drop(mindata[mindata["Date"].dt.year == 2015].index)
mindata = mindata.sort_values(by="Date")
mindata["Date"] = mindata["Date"].dt.strftime('%m-%d %H:%M:%S')
minline = mindata.groupby(by="Date").min()
minline = minline["Data_Value"]
#print(minline)

mindata2015["Date"] = mindata2015["Date"].dt.strftime('%m-%d %H:%M:%S')
minscat2015 = mindata2015.groupby(by="Date").min()
minscat2015 = minscat2015["Data_Value"]
minscat2015mask = minscat2015 < minline
minscat2015 = minscat2015[minscat2015mask]
#print(minscat2015)

maxdata = datadf[datadf["Element"]=="TMAX"]
maxdata2015 = maxdata[maxdata["Date"].dt.year == 2015]
maxdata = maxdata.drop(maxdata[maxdata["Date"].dt.year == 2015].index)
maxdata = maxdata.sort_values(by="Date")
maxdata["Date"] = maxdata["Date"].dt.strftime('%m-%d %H:%M:%S')
maxline = maxdata.groupby(by="Date").max()
maxline = maxline["Data_Value"]
#print(maxline)

maxdata2015["Date"] = maxdata2015["Date"].dt.strftime('%m-%d %H:%M:%S')
maxscat2015 = maxdata2015.groupby(by="Date").max()
maxscat2015 = maxscat2015["Data_Value"]
maxscat2015mask = maxscat2015 > maxline
maxscat2015 = maxscat2015[maxscat2015mask]
print(maxscat2015)

fig, ax = plt.subplots()
ax.plot(minline,'b-',maxline,'r-')
ax.plot(minscat2015, ".", color="green")
ax.plot(maxscat2015, ".", color="black")
fig.gca().fill_between(range(len(minline)), 
                        minline, maxline, 
                        facecolor='purple', 
                        alpha=0.25)
month_starts = [14,44,75,105,136,166,196,227,257,288,318,348]
month_names = ['Jan','Feb','Mar','Apr','May','Jun',
               'Jul','Aug','Sep','Oct','Nov','Dec']
ax.set_xticks(month_starts)
ax.set_xticklabels(month_names)
plt.xlabel("Months")
plt.ylim(-45,45)
plt.ylabel("Temperature (C°)")
plt.title("Record Temperatures (2005-2014) in Ann Arbor, Michigan, U.S.A,\nwith 2015 Record Breaking Temperatures")
plt.legend(["Record Low Temperatures (2005-2014)", "Record High Temperatures (2005-2014)", "Record Breaking Low Temperature (2015)", "Record Breaking High Temperature (2015)"])
plt.show()
