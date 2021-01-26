# -*- coding: utf-8 -*-

import pandas as pd
from zipfile import ZipFile
import glob, csv, os  #, requests, csv
import fnmatch

quotes_hdr = ['symbol', 'quotedate', 'open', 'high', 'low', 'close', 'volume', 'adjustedclose']   # quotedate == DataDate


fn1 =[]
for filepath in glob.iglob(r'D:\\jon\\*.zip'):          #  D:\Jon\optionstats\2016_\Sample_L3_20160105.zip\
    fn1.append(filepath)
    # print(len(fn1))    # filepath is 13 zip files
    
allfiles = []
pattern = '*quotes*.csv'
    
flist = []
matching = []
file0 = pd.DataFrame()

for x in range(len(fn1)):    # print zip files 
  #  print(fn1[x])
    p = fn1[x]         #     #\\"')
    with ZipFile(p) as myzip:
        list1 = myzip.namelist()
        # print(x)
        # print(list1)  
        # print(len(list1))#myzip.namelist())  #filelist) 
        for y in range(len(list1)):
            print(list1[y])
            flist.append(list1[y])   #fnmatch.filter(list[y], pattern))# if len(list1)==0:
## ArithmeticError

print(len(flist))


matching = fnmatch.filter(flist, pattern)
print(len(matching))


"""
for z in range(len(matching)):
    allfiles = pd.concat([file0, pd.read_csv(matching[z], low_memory=False, header=False)].head(3))
                
            
            
print(len(matching))    # break
allfiles.to_csv("d.csv", header=cols)
    






    # else:
# print(len(flist))    
            
print(flist)



# for k in range(len(flist)):
    
    
    
    
      # fp = str((') flist[k].astpe(str) +str("'")
      # print(flist[k])
     if  sub in flist[k]:
         print(flist[l])
         allfiles.append(flist[k])
     else:
         break

    # for file in flist:
        
        
        
    #     if fnmatch.fnmatch(file, pattern):
    #     #    print(file)
                        
    # # if fnmatch.fnmatchcase(filena, patt2):
            
print(allfiles)


     
     if fnmatch.fnmatchcase(flist[k], pattern):
         allfiles.append(filename)
         print(allfiles)
print(len(allfiles))  #_csv))





    
    for mf in myzip.filelist:
        with myzip.open(mf.filename) as myfile:
            mc = myfile.read()
            c = csv.StringIO(mc.decode())
            for row in c:
                print(row)
    
    
        
    
    
    
    
    
    
    for filename in p:               #zip.extractall():  # each element in fn1   
        if fnmatch.fnmatch(filename, pattern):
            allfiles.append(filename)
print(len(allfiles))  #_csv))














for x in range(len(fn1)):
    for filename in os.path(fn1):  # each element in fn1   
        if fnmatch.fnmatch(filename, pattern):
            allfiles.append(filename)
        #    allfile_csv = [] 








""
import fnmatch
import os
import pandas as pd
from zipfile import ZipFile

#set file pattern
pattern = '*.zip'

#initialize variables
df_master = pd.DataFrame()


#crawl entire directory in root folder
for root, dirs, files in os.walk("D:\\jon\\"):
    #filter files that match pattern of .zip
    for filename in fnmatch.filter(files, pattern):
        #
        zip_file = ZipFile(os.path.join(root, filename))
        for text_file in zip_file.infolist():
            if text_file.filename.endswith('Bezirke.csv'):
                df = pd.read_csv(zip_file.open(text_file.filename),
                                 delimiter=';',
                                 header=0)
                                
                df_master = pd.concat([df_master, df])
#sort index field Timestamp
df_master.sort_index(inplace=True)

#print master dataframe info
print(df_master.info())

frame.to_csv( "combined.csv", encoding='utf-8-sig')







for text_file in zip_file.infolist():
    if text_file.filename.endswith('Bezirke.csv'):
        df = pd.read_csv(zip_file.open(text_file.filename),
            delimiter=';',
            header=0,
            index_col=['Timestamp'],
            parse_dates=['Timestamp']
            )
        if not flag:
            df_master = df
            flag = True
        else:
            df_master = pd.concat([df_master, df])
            
            
            

        
   #     for name in allfiles:
   # # print(i)
           
   #         allfile_csv.append(name)     
        
# os.chdir("D:\\jon\\")


combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])



df_master = pd.DataFrame()
# flag = False
# allfiles = filename.contains('optionstats')

        
# print(len(
allfile_csv=[]   


for filename in allfiles:    
    zip_file = ZipFile(filename)
    for text_file in os.dir('.'):            
        if fnmatch.fnmatch(text_file, pattern)==True:     
            allfile_csv.append(text_file)                   
            # df = pd.read_csv(zip_file.open(text_file.filename))
            # df_master = pd.concat([df_master, df])

print(len(allfile_csv))#   df_master.info())


import fnmatch, os

  #]
for name in os.listdir('.'):
    if fnmatch.fnmatch(name, pattern)==True:
        allfile_csv.append(name)             # name is the file name
 
print(allfile_csv)  #.tolist())       
    #    print('Filename: %-25s %s' % (name, fnmatch.fnmatch(name, pattern)))
    

import glob, zipfile, os
import pandas as pd

dfs = []
for filename in os.listdir("D:\\jon\\"):
    if filename.endswith('.zip'):
        zip_file = os.path.join(dir_name, filename)
        zf = zipfile.ZipFile(zip_file)
        print(zf.namelist())
       # dfs += [pd.read_csv(zf.open(f), header=None, sep=";") for f in zf.namelist()]
# df = pd.concat(dfs,ignore_index=True)

"""