# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:58:29 2021

@author: WW Ent
"""
import pandas as pd
# df2 = pd.read_excel('D:\\jon\\L2_options_20201119.xlsx')  #, low_memory=False)    # ExcelFile or read_excel all got errors

#   headers, you need this!
#  ['UnderlyingSymbol', 'UnderlyingPrice', 'Exchange', 'OptionSymbol', 'OptionExt', 'Type', 'Expiration', 'DataDate', 'Strike', 'Last', 'Bid', 'Ask', 'Volume', 'OpenInterest', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega', 'AKA']

list8 = ['FIVN', 'TWLO', 'OKTA', 'AMD', 'AAPL']
list7 = ['MTCH', 'SNBR', 'PAYC', 'TXN', 'WING']

df3= pd.read_csv('D:\\Jon\\retrieval_ops\\output\\10ops2.csv', low_memory=False) 
df3[df3.UnderlyingSymbol.isin(list7)].drop(columns = ['AKA', 'Edate', 'DDate', 'diff', 'diff2']).to_csv("10ops_p1.csv", index=False)
df3[df3.UnderlyingSymbol.isin(list8)].drop(columns = ['AKA', 'Edate', 'DDate', 'diff', 'diff2']).to_csv("10ops_p2.csv", index=False)
"""
.to_csv("10ops3.csv")
            
                 
                 D:\\jon\\L2_options_20201119.csv', low_memory=False)   #  , chunksize=1000000)
# df3['und']
# df3.info()        #   describe()          #ail()
# print(df3['UnderlyingSymbol'].nunique())
# print(df2['symbol'].index))  #, index_col=0, comment='#')   # pd.read_excel('tmp.xlsx', index_col=0, comment='#')  

df3.sample(frac=0.05).to_csv("D:\\jon\\sample_op500.csv", index=False)  #ail(3)


df1 = pd.ExcelFile("D:\\Jon\\")

col0 = []
for col in df3.columns:
    col0.append(col)
    
print(col0)

print(df1.head)
"""