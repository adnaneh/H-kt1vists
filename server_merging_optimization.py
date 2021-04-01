# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 17:03:06 2021

@author: adnane
"""

# optimize servers by merging

import pandas as pd

dummy_solution = 'C:/Users/adnane/Documents/GitHub/H-kt1vists/exemple.csv'

df = pd.read_csv(dummy_solution).to_numpy()

2_merge_map = {'tiny_1':'tiny_2'}

col = df['1']

c1 = -1
c2 = -1
delet_rows = []
services_list = [] 
for i in range (len(df)):
    row = df.iloc[i]
    if row[0] == 'tiny_1':
        if c1 == -1:
            c1 = i
            continue
        else:
            couple = (c1, i)
            row_1 = df.iloc[c1]
            row_2 = df.iloc[c2]
            services = row_1[1:] + row_2[1:]
            services_list.append(services)
            delet_rows.append(c1)
            delet_rows.append(i)
            
res = []
for i in range (len(df)):
    if i in delet_rows:
        continue
    row = df.iloc[i]
    res.append(row)

res = 
    