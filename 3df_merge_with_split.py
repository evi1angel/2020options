# -*- coding: utf-8 -*-

import pandas as pd
from zipfile import ZipFile
import glob, csv, os, os.path  #, requests, csv
import fnmatch

# list0 = ['AMD', 'TAL', 'DECK', 'FIVN', 'ILMN', 'MTCH', 'OKTA', 'ILMN', 'EAT', 'ETSY', 'EVBG', 'NOVT', 'TDOC', 'TWLO']

list0 = ['AAN', 'AAPL', 'ADBE', 'ADSK', 'AJRD', 'ALNY', 'ALRM', 'AMD', 'AMED', 'AMN', 'APH', 'ARNA', 'ASML', 'AVGO', 'AYX', 'AZUL', 'BABA', 'BL', 'BLD']
list1 = ['BOOM', 'BRKS', 'CAKE', 'CCL', 'CCS', 'CHGG', 'CRSP', 'CVNA', 'DECK', 'DG', 'DPZ', 'DXCM', 'EAT', 'EDU', 'ETSY', 'EVBG', 'EXAS', 'FATE']
list2 = ['FIVN', 'FN', 'FRPT', 'GOOS', 'GRUB', 'HQY', 'HTHT', 'HZNP', 'ILMN', 'IRDM', 'IRTC', 'IT', 'ITGR', 'LITE', 'MANT', 'MBUU', 'MELI', 'MOH']
list3 =['MPWR', 'MRVL', 'MTCH', 'MTOR', 'MTZ', 'NOVT', 'NVDA', 'NVEE', 'NVRO', 'OKTA', 'OLED', 'OLLI','PAYC', 'PENN', 'PGR', 'POOL', 'PRLB', 'RCL']
list4 = ['RGEN', 'RMD', 'RNG', 'ROKU', 'ROM', 'SIVB', 'SMTC', 'SNBR', 'SPWR', 'SPXL', 'SQ', 'SRPT', 'STMP', 'TAL', 'TDOC', 'TKR']
list5 = ['TREX', 'TRUP', 'TTD', 'TTWO', 'TWLO', 'TXN', 'WAT', 'WCN', 'WDAY', 'WING', 'WPM', 'Z', 'ZGNX']
 
list6 = ['FIVN', 'TWLO', 'OKTA', 'AMD', 'MTCH', 'SNBR', 'PAYC', 'TXN', 'AAPL', 'WING']
list8 = ['FIVN', 'TWLO', 'OKTA', 'AMD', 'AAPL']
list7 = ['MTCH', 'SNBR', 'PAYC', 'TXN', 'WING']

#  options headers, you need this!  original order
col_options = ['UnderlyingSymbol', 'UnderlyingPrice', 'Exchange', 'OptionSymbol', 'OptionExt', 'Type', 'Expiration', 'DataDate', 'Strike', 'Last', 'Bid', 'Ask', 'Volume', 'OpenInterest', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega']  #, 'AKA']
# stocks header            
options_hdr = ['UnderlyingSymbol', 'DataDate', 'UnderlyingPrice', 'Exchange', 'OptionSymbol', 'OptionExt', 'Type', 'Expiration', 'Strike', 'Last', 'Bid', 'Ask', 'Volume', 'OpenInterest', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega']  #, 'AKA']
# 

quotes_hdr = ['symbol', 'quotedate', 'open', 'high', 'low', 'close', 'volume', 'adjustedclose']  
# stats header!!
stats_hdr = ['symbol', 'quotedate', 'iv30call', 'iv30put', 'iv30mean', 'callvol', 'putvol', 'totalvol', 'calloi', 'putoi', 'comment']


df0 = pd.read_csv("10ops_p1.csv", low_memory=False).reindex(columns = options_hdr) 

# print(df0.UnderlyingSymbol.nunique())

# print(list0+list1+list2+list3+list4+list5)

# l_check = [item for item in (list0+list1+list2+list3+list4+list5) if item not in df0.UnderlyingSymbol.tolist()]
# print(l_check)


# .nunique()   # read_csv("D:\\jon\\retrieval\\L2_options_20201023.csv", low_memory=False)   #102020.zip\\")

#  df_stats = pd.read_csv("1023_1112stats.csv", low_memory=False) 
# df_quotes = pd.read_csv("D\\jon\\1023_1112quotes.csv", low_memory=False) 

df1 = pd.merge(pd.read_csv("10stats.csv", low_memory=False), pd.read_csv("10quotes.csv", low_memory=False), how='inner') 
# df1.to_csv("outer.csv") #  .to_csv("test.csv", index=False)  #   right_on='Plant Code')
df0[df0.UnderlyingSymbol.isin(list7)].rename(columns={'UnderlyingSymbol':'symbol', 'DataDate':'quotedate'}).merge(df1[df1.symbol.isin(list7)], on=['symbol', 'quotedate'], how='left').to_csv("10merged_p1.csv", index=False) 

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
    

