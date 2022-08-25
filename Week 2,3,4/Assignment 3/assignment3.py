import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

np.random.seed(12345)

#given y value
y = 41000

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

df["mean"] = df.mean(axis=1)
means = df["mean"].array
years = ["1992","1993","1994","1995"]
ci1992 = st.t.interval(0.95, len(df.loc[1992])-1, loc=np.mean(df.loc[1992]), scale=st.sem(df.loc[1992]))
ci1993 = st.t.interval(0.95, len(df.loc[1993])-1, loc=np.mean(df.loc[1993]), scale=st.sem(df.loc[1993]))
ci1994 = st.t.interval(0.95, len(df.loc[1994])-1, loc=np.mean(df.loc[1994]), scale=st.sem(df.loc[1994]))
ci1995 = st.t.interval(0.95, len(df.loc[1995])-1, loc=np.mean(df.loc[1995]), scale=st.sem(df.loc[1995]))
ci = [ci1992,ci1993,ci1994,ci1995]
y_r = [means[i] - ci[i][1] for i in range(len(ci))]
colors = []
for i in ci:
    if y < i[0]:
        colors.append("red")
    elif y > i[1]:
        colors.append("blue")
    else:
        colors.append("#DCDCDC")

fig, ax = plt.subplots()
plt.bar(x=years,height=means, yerr=y_r, align="center", color=colors, edgecolor="black")
line_x = ["1992","1993","1994","1995"]
line_y = [y,y,y,y]
plt.plot(line_x,line_y, color="black")
plt.ylim(0,57000)
legend_colors = {"Y Value Above Confidence Interval" : "red", "Y Value Below Confidence Interval" : "blue", "Y Value in Confidence Interval" : "#DCDCDC"}
labels = list(legend_colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=legend_colors[label]) for label in labels]
plt.legend(handles, labels, loc=2)
plt.xlabel("Year")
plt.ylabel("Mean Values")
plt.title("Easiest option : Mean Values with 95% Confidence Interval\nY value = {}".format(y))
plt.show()