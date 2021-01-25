# -*- coding: utf-8 -*-

import pandas as pd
from zipfile import ZipFile
import glob, csv, os, os.path  #, requests, csv
import fnmatch

list0 = ['AMD', 'TAL', 'DECK', 'FIVN', 'ILMN', 'MTCH', 'OKTA', 'ILMN', 'EAT', 'ETSY', 'EVBG', 'NOVT', 'TDOC', 'TWLO']

#  options headers, you need this!
col_options = ['UnderlyingSymbol', 'UnderlyingPrice', 'Exchange', 'OptionSymbol', 'OptionExt', 'Type', 'Expiration', 'DataDate', 'Strike', 'Last', 'Bid', 'Ask', 'Volume', 'OpenInterest', 'IV', 'Delta', 'Gamma', 'Theta', 'Vega', 'AKA']

df0 = pd.DataFrame()  #  (columns = col_options)    # read_csv("D:\\jon\\retrieval\\L2_options_20201023.csv", low_memory=False)   #102020.zip\\")

fn0 =[]
for filepath in glob.iglob(r'D:\\jon\\retrieval\\*.csv'):
    fn0.append(filepath)
 #   print(fn0)    #filepath)

print(len(fn0))

ind = [] 
n = 1      # ind = [1,2,3]
max0 = int(len(fn0))

print(n<max0)

str2 ="new"


while n < max0:
    # print(n)
    ind.append(n)
    for i in fn0:
    #    infile_index = str1 + '.' + str(i) + '.csv'
        outfile_index = str2 + str(n) + ".csv"
        print("reading: # " +str(i)+ " ")
        df_tst = pd.read_csv(i, low_memory=False) 
        pd.concat([df_tst[df_tst.UnderlyingSymbol.isin(list0)], df0]).to_csv(outfile_index, index=False)   #  ue, date                                                     
        n = n+1                                                         

print("done!")
    
# dfs.to_csv("0125_2run.csv", index=False)
"""







ind = []       # ind = [1,2,3]
max = 76
n = 35
while n < max:
    # print(n)
    ind.append(n)
    n = n+1

str1 = 'flow_matched_fy19ytd_cy19_m06'
str2 = 'bd_nonull'
for i in ind:
    infile_index = str1 + '.' + str(i) + '.csv'
    outfile_index = str2 + '.' + str(i) + '.csv'
     print("Importing " + infile_index)
    df1 = pd.read_csv(infile_index, names=list0, sep=',',quotechar='"', quoting=1, engine='python').set_index('new_id')
    df5 = pd.DataFrame({'n': df1[~df1.birth_dt.isnull()].groupby("new_id")['birth_dt'].nunique()>1})
    print(df1[df1.index.isin(df5[df5.n==True].index.tolist())].shape)
    df1[df1.index.isin(df5[df5.n==True].index.tolist())].to_csv(outfile_index, index=True, date_format='%Y-%m-%d') #.sort_values('new_id')  #index

  #  dw_id2' : 'new_id'}).reindex(columns=list1).sample(n=1000).to_csv("sample1000.tsv",sep='\t', index=False, header=False, quoting=0,quotechar='"')
    print("Finish work on " + infile_index)
    
  #  .i.
  # df.drop(columns=['new_id', 'ncic_code', 'flag']).rename(columns={'new_id2' : 'new_id'}).reindex(columns=list1).to_csv(outfile_index,sep='\t', index=False, header=False, quoting=0, quotechar='"')
  
#    df.drop(columns=['new_id', 'ncic_code', 'flag']).rename(columns={'new_id2' : 'new_id'}).reindex(columns=list1).to_csv(outfile_index, sep='\t', index=False, header=True, quoting=0, quotechar='"')
  
  # sample files  
  # df.drop(columns=['new_id', 'ncic_code', 'flag']).rename(columns={'new_id2' : 'new_id'}).reindex(columns=list1).sample(n=10).to_csv('stg_sample10.tsv', sep='\t', index=False, header=True, quoting=0, quotechar='"')
 
    
    
    # to_csv("sample200.tsv",sep='\t', index=False, header=False, quoting=0,quotechar='"')# end of for loop
    # to_csv("sample200.tsv",sep='\t', index=False, header=False, quoting=0,quotechar='"')# end of for loop

print("Exit ~ FOR ~ Loop, well done!")
#  .append(df5)




ind = []       # ind = [1,2,3]
max = 76
n = 35
while n < max:
    # print(n)
    ind.append(n)
    n = n+1
# df = pd.DataFrame()  #columns=list1)
#str2 = "flow_matched_fy19ytd.st."
str1 = 'flow_matched_fy19ytd_cy19_m06'
str2 = 'bd_nonull'
for i in ind:
  # no need if first df
    
 #  print(i)
    infile_index = str1 + '.' + str(i) + '.csv'
    outfile_index = str2 + '.' + str(i) + '.csv'
    # print(infile_index)
    # print(outfile_index)
    
    print("Importing " + infile_index)
    df1 = pd.read_csv(infile_index, names=list0, sep=',',quotechar='"', quoting=1, engine='python').set_index('new_id')
   
  # df3 = df1.loc[df1.birth_dt.isnull()]

#df2 =df1[~df1.birth_dt.isnull()].copy()
#df2['b_yr'] = df2['birth_dt'][-4:]
#
#df2s = df2[~df2.b_yr.isnull()]  #.head  #.shape
#df2s.to_csv('d2s.csv')
# df3.shape
#
#df2s.b_yr.astype(int)
#df4 = df2s[df2s.b_yr < 1920].drop(columns=(['b_yr']))
#
#df4.shape
  # datetime.date(1920,1,1)]
  # this include multiple bday such as 4 rows of 02/08/1887
    df5 = pd.DataFrame({'n': df1[~df1.birth_dt.isnull()].groupby("new_id")['birth_dt'].nunique()>1})
   # df5[df5.n==False].to_csv("df5_false.csv")
    print(df1[df1.index.isin(df5[df5.n==True].index.tolist())].shape)
    df1[df1.index.isin(df5[df5.n==True].index.tolist())].to_csv(outfile_index, index=True, date_format='%Y-%m-%d') #.sort_values('new_id')  #index

  #  df = pd.read_csv(infile_index, sep=',',quotechar='"', quoting=1, engine='python')
  #  df['new_id2'].astype(int)
    
  #  df['new_id2'] = df['new_id'].apply(lambda x: x * 3 + 8699)
#    df['new_id'].astype(int)
#    df['new_id2'] = df['new_id'].apply(lambda x: x*3 + 8699)
#    print("Writing out " + outfile_index)
#    df['event_date'] = pd.to_datetime(df['event_date'])
   # df.i.drop(columns=['new_id']).rename(columns={'new_id2' : 'new_id'}).reindex(columns=list1).
 #  df.i.to_csv(outfile_index,sep='\t', index=False, header=False, quoting=0, quotechar='"')
 #  df.drop(columns=['new_id']).rename(columns={'new_id2' : 'new_id'}).reindex(columns=list1).sample(n=1000).to_csv("sample1000.tsv",sep='\t', index=False, header=False, quoting=0,quotechar='"')
    print("Finish work on " + infile_index)
    
  #  .i.
  # df.drop(columns=['new_id', 'ncic_code', 'flag']).rename(columns={'new_id2' : 'new_id'}).reindex(columns=list1).to_csv(outfile_index,sep='\t', index=False, header=False, quoting=0, quotechar='"')
  
#    df.drop(columns=['new_id', 'ncic_code', 'flag']).rename(columns={'new_id2' : 'new_id'}).reindex(columns=list1).to_csv(outfile_index, sep='\t', index=False, header=True, quoting=0, quotechar='"')
  
  # sample files  
  # df.drop(columns=['new_id', 'ncic_code', 'flag']).rename(columns={'new_id2' : 'new_id'}).reindex(columns=list1).sample(n=10).to_csv('stg_sample10.tsv', sep='\t', index=False, header=True, quoting=0, quotechar='"')
 
    
    
    # to_csv("sample200.tsv",sep='\t', index=False, header=False, quoting=0,quotechar='"')# end of for loop
    # to_csv("sample200.tsv",sep='\t', index=False, header=False, quoting=0,quotechar='"')# end of for loop

print("Exit ~ FOR ~ Loop, well done!")
#  .append(df5)


"""