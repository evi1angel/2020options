# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime as dt 
# from zipfile import ZipFile
import glob, csv, os, os.path  #, requests, csv
import fnmatch

# list0 = #  ['AMD', 'TAL', 'DECK', 'FIVN', 'ILMN', 'MTCH', 'OKTA', 'ILMN', 'EAT', 'ETSY', 'EVBG', 'NOVT', 'TDOC', 'TWLO']
# list0 = ['AAN', 'AAPL', 'ADBE', 'ADSK', 'AJRD', 'ALNY', 'ALRM', 'AMD', 'AMED', 'AMN', 'APH', 'ARNA', 'ASML', 'AVGO', 'AYX', 'AZUL', 'BABA', 'BL', 'BLD', 'BOOM', 'BRKS', 'CAKE', 'CCL', 'CCS', 'CHGG', 'CRSP', 'CVNA', 'DECK', 'DG', 'DPZ', 'DXCM', 'EAT', 'EDU', 'ETSY', 'EVBG', 'EXAS', 'FATE', 'FIVN', 'FN', 'FRPT', 'GOOS', 'GRUB', 'HQY', 'HTHT', 'HZNP', 'ILMN', 'IRDM', 'IRTC', 'IT', 'ITGR', 'LITE', 'MANT', 'MBUU', 'MELI', 'MOH', 'MPWR', 'MRVL', 'MTCH', 'MTOR', 'MTZ', 'NOVT', 'NVDA', 'NVEE', 'NVRO', 'OKTA', 'OLED', 'OLLI', 'PAYC', 'PENN', 'PGR', 'POOL', 'PRLB', 'RCL', 'RGEN', 'RMD', 'RNG', 'ROKU', 'ROM', 'SIVB', 'SMTC', 'SNBR', 'SPWR', 'SPXL', 'SQ', 'SRPT', 'STPM', 'TAL', 'TDOC', 'TKR', 'TREX', 'TRUP', 'TTD', 'TTWO', 'TWLO', 'TXN', 'WAT', 'WCN', 'WDAY', 'WING', 'WPM', 'Z', 'ZGNX']
#  options headers, you need this!
col_options = ['UnderlyingSymbol', 'UnderlyingPrice', 'Exchange', 'OptionSymbol', 'OptionExt', 'Type', 'Expiration', 'DataDate', 'Strike', 'Last', 'Bid', 'Ask', 'Volume', 'OpenInterest', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega', 'AKA']
quotes_hdr = ['symbol', 'quotedate', 'open', 'high', 'low', 'close', 'volume', 'adjustedclose']  

list6 = ['FIVN', 'TWLO', 'OKTA', 'AMD', 'MTCH', 'SNBR', 'PAYC', 'TXN', 'AAPL', 'WING']
# df0 = pd.DataFrame()  #  (columns = col_options)    # read_csv("D:\\jon\\retrieval\\L2_options_20201023.csv", low_memory=False)   #102020.zip\\")
fn0 =[]
for filepath in glob.iglob(r'D:\\jon\\retrieval_ops\\*.csv'):
    fn0.append(filepath)
 #   print(fn0)    #filepath)
print(len(fn0))
ind = [] 
n = 1      # ind = [1,2,3]
max0 = int(len(fn0))

# print(n<max0)
str2 ="D:\\Jon\\retrieval_ops\\output\\new"
while n < max0:
    # print(n)
    ind.append(n)
    for i in fn0:
    #    infile_index = str1 + '.' + str(i) + '.csv'
        outfile_index = str2 + str(n)   #  +".csv"
        print("reading: # " +str(i)+ " ")
        df_tst = pd.read_csv(i, low_memory=False) 
        if n==1:
            df_tst['Edate'] = pd.to_datetime(df_tst.Expiration)#  df_tst['Expiration'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
            df_tst['DDate'] = pd.to_datetime(df_tst.DataDate)   #'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
            df_tst['diff'] = (df_tst['Edate'] - df_tst['DDate'])
            df_tst['diff2'] = df_tst['diff'].astype('timedelta64[D]').astype(int)#  change symbol or Underlyingsymol here  
            df_tst[df_tst.diff2 <= 90][df_tst.UnderlyingSymbol.isin(list6)].to_csv(outfile_index, header=True, index=False)
        else:
            df_tst['Edate'] = pd.to_datetime(df_tst.Expiration)#  df_tst['Expiration'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
            df_tst['DDate'] = pd.to_datetime(df_tst.DataDate)   #'].apply(lambda x: pd.Timestamp(x).strftime('%Y-%m-%d'))
            df_tst['diff'] = (df_tst['Edate'] - df_tst['DDate'])
            df_tst['diff2'] = df_tst['diff'].astype('timedelta64[D]').astype(int)#  ue, date       
            df_tst[df_tst.diff2 <= 90][df_tst.UnderlyingSymbol.isin(list6)].to_csv(outfile_index, header=False, index=False)                                               
        n = n+1                                                         
print("done!")
    

