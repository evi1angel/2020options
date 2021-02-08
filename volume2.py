# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 00:57:36 2021

@author: pinkj
"""
import pandas as pd

# cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#         'Price': [22000,25000,27000,15000]
#         }
df = pd.read_csv("c:\\2021options\\bbby_5yr.csv", low_memory=False)    # DataFrame(cars, columns = ['Brand', 'Price'])
df.columns
df.head(5)
# print(df.shape[0])      # of rows        
# print(df.shape[1])      # of cols

# length = len(df.index)
# print (length)

# # print ("Length of data frame is %s" %length)
# # print ("Headers of data frame is %s" %df.columns)

# shape1 = df.shape
# rows = shape1[0]
# rows = rows-1
# print ("Number of rows is %s" %rows)
# print ("Number of colums is %s" %shape1[1])

# print ("Number of rows is %s" %rows)
# print ("Number of colums is %s" %shape1[1])

ind0 = []
ind1 = []
for ind in df.index:
    if ind > 1:
       if df['high'][ind] >= 0.15*df['high'][ind-1]:
           ind0.append(ind)   #  return ind  #  print("Current price is higher than last price.")
      
for ind in df.index:
    if ind >1: 
        if df['volume'][ind] >= 2*lastv = df['volume'][ind-1]:
           ind1.append(ind)   #  return ind              

df[df.index.isin(ind0) & df.index.isin(ind1)].to_csv("c:\\2021options\\bbby_5yr_jump.csv", index=False)        
