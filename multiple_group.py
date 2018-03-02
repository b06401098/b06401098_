# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:26:08 2018

@author: user
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Ntu_Orders.csv')

df['new_DateId'] = pd.to_datetime(df['DateId'].astype(str),format='%Y%m%d')

data = df.groupby(by=['LevelOneCategoryName','new_DateId'])['Quantity'].sum().reset_index()

plot_list = []

for i in set(data['LevelOneCategoryName'].values):
    plot_list.append(data[data['LevelOneCategoryName']==i].groupby(by='new_DateId')['Quantity'].sum())

fig, ((a,b),(c,d),(e,f)) = plt.subplots(3,2,figsize=(100,100))

a.plot(plot_list[0])
b.plot(plot_list[1])
c.plot(plot_list[2])
d.plot(plot_list[3])
e.plot(plot_list[4])
f.plot(plot_list[5])    