# -*- coding: utf-8 -*-

import pandas as pd
from zipfile import ZipFile
import glob, csv, os, os.path  #, requests, csv
import fnmatch

list0 = ['AMD', 'TAL', 'DECK', 'FIVN', 'ILMN', 'MTCH', 'OKTA', 'ILMN', 'EAT', 'ETSY', 'EVBG', 'NOVT', 'TDOC', 'TWLO']

#  options headers, you need this!
col_options = ['UnderlyingSymbol', 'UnderlyingPrice', 'Exchange', 'OptionSymbol', 'OptionExt', 'Type', 'Expiration', 'DataDate', 'Strike', 'Last', 'Bid', 'Ask', 'Volume', 'OpenInterest', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega', 'AKA']
              

quotes_hdr = ['symbol', 'quotedate', 'open', 'high', 'low', 'close', 'volume', 'adjustedclose']  

# df0 = pd.DataFrame()  #  (columns = col_options)    # read_csv("D:\\jon\\retrieval\\L2_options_20201023.csv", low_memory=False)   #102020.zip\\")

# list3 = ['TAL']

fn0 =[]
for filepath in glob.iglob(r'D:\\jon\\retrieval\\*.csv'):
    fn0.append(filepath)
 #   print(fn0)    #filepath)

print(len(fn0))

ind = [] 
n = 1      # ind = [1,2,3]
max0 = int(len(fn0))

# print(n<max0)
str2 ="D:\\Jon\\retrieval\\output\\new"
while n < max0:
    # print(n)
    ind.append(n)
    for i in fn0:
    #    infile_index = str1 + '.' + str(i) + '.csv'
        outfile_index = str2 + str(n)   #  +".csv"
        print("reading: # " +str(i)+ " ")
        df_tst = pd.read_csv(i, low_memory=False) 
        if n==1:
            df_tst[df_tst.symbol.isin(list0)].to_csv(outfile_index, header=True, index=False)         #  change symbol or Underlyingsymol here  
        else:
            df_tst[df_tst.symbol.isin(list0)].to_csv(outfile_index, header=False, index=False)  #  ue, date                                                     
        n = n+1                                                         
print("done!")
    

