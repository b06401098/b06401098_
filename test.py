# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 15:50:43 2018

@author: user
"""

import pandas as pd

df = pd.read_csv('Ntu_Orders.csv')

df.head()

df.tail()

df.shape
df.info()

df['new_DateId'] = pd.to_datetime(df['DateId'].astype(str),format='%Y%m%d')

df.info()
df.head()

df['Quantity'].head()

df.loc[1000:1005,'Quantity']

df.loc[1000:1005,['new_DateId','Quantity']]

df[df['Quantity']>1]

data = df.groupby(by='new_DateId')['Quantity'].sum()

data.plot()