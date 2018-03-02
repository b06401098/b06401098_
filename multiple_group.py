# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 14:26:08 2018

@author: user
"""

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)

df = pd.read_csv('Ntu_Orders.csv')

df['new_DateId'] = pd.to_datetime(df['DateId'].astype(str),format='%Y%m%d')

data = df.groupby(by=['LevelOneCategoryName','new_DateId'])['Quantity'].sum().reset_index()

plot_list = []

fig, ((a,b),(c,d),(e,f)) = plt.subplots(3,2,figsize=(100,100))

layout_list = [a,b,c,d,e,f]

index = 0
for i in set(data['LevelOneCategoryName'].values):
    plot_list.append(data[data['LevelOneCategoryName']==i].groupby(by='new_DateId')['Quantity'].sum())
    layout_list[index].set_title(i,fontproperties=font)
    print(i)
    index = index+1
index = 0
for i in layout_list:
    i.plot(plot_list[index])
    index = index+1
    