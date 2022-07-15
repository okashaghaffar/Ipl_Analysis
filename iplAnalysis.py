# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 08:24:24 2022

@author: PC
"""
print("IPL 2020 Analysis")
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
ipl=pd.read_csv("ipdata.csv")
r,c=ipl.shape
print("Total rows are",r,"total Columns are ",c)
Total_Values=np.product((r,c))
print("Total Cells utilized are :",Total_Values)
missing_Values=ipl.isnull().sum().sum()
print("missing values are: ",missing_Values)
gp=ipl.groupby("venue").match_id.count()
newgp=pd.DataFrame({"Matches":ipl.groupby("venue").match_id.count()}).reset_index()
print(newgp)
plt.figure(figsize=(100,40))
plt.title("MATCHES AND VENUES")
sns.barplot(data=newgp, x="venue",y="Matches")
plt.show()



toss_percent=pd.DataFrame({"Toss won":ipl.groupby("toss_winner").toss_winner.count()}).reset_index()
total_tosses=(toss_percent["Toss won"].sum())
print(total_tosses)

#toss_percent.groupby(["toss_winner"]).sum().plot(kind="pie",y="Toss won",autopct='%1.0f%%')
plt.pie(toss_percent['Toss won'],labels=toss_percent['toss_winner'],autopct='%1.0f%%')
plt.Figure(figsize=(70,30))
plt.title("Toss winning percentage")
plt.legend()
plt.show()



