# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:20:37 2018

@author: user
"""

import pandas as pd

df = pd.read_csv('Ntu_Orders.csv')

data = df.groupby(by='DateId')['Quantity'].sum()

data = pd.DataFrame(data).sort_values(by='Quantity',ascending=False)

data.to_csv('example.csv')
