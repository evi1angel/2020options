# -*- coding: utf-8 -*-

import pandas as pd
from zipfile import ZipFile
import glob, csv, os, os.path  #, requests, csv
import fnmatch

# list0 = ['AMD', 'TAL', 'DECK', 'FIVN', 'ILMN', 'MTCH', 'OKTA', 'ILMN', 'EAT', 'ETSY', 'EVBG', 'NOVT', 'TDOC', 'TWLO']

list0 = ['AAN', 'AAPL', 'ADBE', 'ADSK', 'AJRD', 'ALNY', 'ALRM', 'AMD', 'AMED', 'AMN', 'APH', 'ARNA', 'ASML', 'AVGO', 'AYX', 'AZUL', 'BABA', 'BL', 'BLD', 'BOOM', 'BRKS', 'CAKE', 'CCL']
list1 = ['CCS', 'CHGG', 'CRSP', 'CVNA', 'DECK', 'DG', 'DPZ', 'DXCM', 'EAT', 'EDU', 'ETSY', 'EVBG', 'EXAS', 'FATE', 'FIVN', 'FN', 'FRPT', 'GOOS', 'GRUB', 'HQY', 'HTHT', 'HZNP', 'ILMN'] #, '
list2 = ['IRDM', 'IRTC', 'IT', 'ITGR', 'LITE', 'MANT', 'MBUU', 'MELI', 'MOH', 'MPWR', 'MRVL', 'MTCH', 'MTOR', 'MTZ', 'NOVT', 'NVDA', 'NVEE', 'NVRO', 'OKTA', 'OLED', 'OLLI','PAYC', 'PENN']
list3 = ['PGR', 'POOL', 'PRLB', 'RCL', 'RGEN', 'RMD', 'RNG', 'ROKU', 'ROM', 'SIVB', 'SMTC', 'SNBR', 'SPWR', 'SPXL', 'SQ', 'SRPT', 'STPM', 'TAL', 'TDOC', 'TKR', 'TREX', 'TRUP', 'TTD'] 
list4 = ['TTWO', 'TWLO', 'TXN', 'WAT', 'WCN', 'WDAY', 'WING', 'WPM', 'Z', 'ZGNX']
 
#  options headers, you need this!  original order
col_options = ['UnderlyingSymbol', 'UnderlyingPrice', 'Exchange', 'OptionSymbol', 'OptionExt', 'Type', 'Expiration', 'DataDate', 'Strike', 'Last', 'Bid', 'Ask', 'Volume', 'OpenInterest', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega', 'AKA']
# stocks header            
options_hdr = ['UnderlyingSymbol', 'DataDate', 'UnderlyingPrice', 'Exchange', 'OptionSymbol', 'OptionExt', 'Type', 'Expiration', 'Strike', 'Last', 'Bid', 'Ask', 'Volume', 'OpenInterest', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega', 'AKA']
# 

quotes_hdr = ['symbol', 'quotedate', 'open', 'high', 'low', 'close', 'volume', 'adjustedclose']  
# stats header!!
stats_hdr = ['symbol', 'quotedate', 'iv30call', 'iv30put', 'iv30mean', 'callvol', 'putvol', 'totalvol', 'calloi', 'putoi', 'comment']


df0 = pd.read_csv("0401options.csv", low_memory=False).reindex(columns = options_hdr) 

# .nunique()   # read_csv("D:\\jon\\retrieval\\L2_options_20201023.csv", low_memory=False)   #102020.zip\\")

#  df_stats = pd.read_csv("1023_1112stats.csv", low_memory=False) 
# df_quotes = pd.read_csv("D\\jon\\1023_1112quotes.csv", low_memory=False) 

df1 = pd.merge(pd.read_csv("0401stats.csv", low_memory=False), pd.read_csv("0401quotes.csv", low_memory=False), how='inner')  #  .to_csv("test.csv", index=False)  #   right_on='Plant Code')
df0[df0.UnderlyingSymbol.isin(list4)].rename(columns={'UnderlyingSymbol':'symbol', 'DataDate':'quotedate'}).merge(df1[df1.symbol.isin(list4)], on=['symbol', 'quotedate'], how='left').drop(columns =['AKA']).to_csv("0401merged4.csv", index=False) 

# pd.merge(
    
# df0.head()
"""


symbol	quotedate	iv30call	iv30put	iv30mean	callvol	putvol	totalvol	calloi	putoi	comment

pd.concat()

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
        print("Reading: # " +str(i)+ " ")
        df_tst = pd.read_csv(i, low_memory=False) 
        if n==1:
            df_tst[df_tst.symbol.isin(list0)].to_csv(outfile_index, header=True, index=False)         #  change symbol or Underlyingsymol here  
        else:
            df_tst[df_tst.symbol.isin(list0)].to_csv(outfile_index, header=False, index=False)  #  ue, date                                                     
        n = n+1                                                         
print("done!")

"""
    

