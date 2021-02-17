# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:13:20 2021

@author: WW Ent
"""
import requests, time, json, io, os # logging
from datetime import datetime, timedelta #, datetime
start_time = time.time()
import pandas as pd
import time
from io import StringIO
headers = {"x-messari-api-key": "bcc9eae7-e169-4fb7-9984-1aba92ac6e3e"}

df0 = pd.read_csv("Messari_9mkt.csv", low_memory=False)  
df1 = df0[~df0.price_usd.isnull()]
df1.shape    #   2089 x 19 
#  print(len(df1['mkt-pair'].tolist()))  # still 2089

l0= df0['mkt-pair'].tolist()
l0.sort()
print(len(l0))         # 3168


l1= df1['mkt-pair'].tolist()
l1.sort()
print(len(l1))         # 2089

# ## 5 yr, do not changE!!!  ===============================
# l1 = pd.concat([df1[df1.trade_start.str[:4]=='2016'], df1[df1.trade_start.str[:4]=='2017'], df1[df1.trade_start.str[:4]=='2018'], df1[df1.trade_start.str[:4]=='2019'], 
#     df1[df1.trade_start.str[:4]=='2020']])['mkt-pair'].tolist()               #   2044 
# l1.sort()              # ==============================

# #  Unique pair that has reported price trade_start year
# df1[df1.trade_start.str[:4]=='2011']['pair'].nunique()     #  1
# df1[df1.trade_start.str[:4]=='2012']['pair'].nunique()     #  0
# df1[df1.trade_start.str[:4]=='2013']['pair'].nunique()     #  5
# df1[df1.trade_start.str[:4]=='2014']['pair'].nunique()     #  10
# df1[df1.trade_start.str[:4]=='2015']['pair'].nunique()     #  16
# df1[df1.trade_start.str[:4]=='2016']['pair'].nunique()     #  78
# df1[df1.trade_start.str[:4]=='2017']['pair'].nunique()     #  214
# df1[df1.trade_start.str[:4]=='2018']['pair'].nunique()     #  320
# df1[df1.trade_start.str[:4]=='2019']['pair'].nunique()     #  332
# df1[df1.trade_start.str[:4]=='2020']['pair'].nunique()     #  645

str1_list = ["2017-11-02T00:00:15.000Z&end=2017-11-23"]  #"]
for x in range(len(str1_list)):
    for i in range(len(l0)):  
        # if i < 1361:
        #     pass
        # else: 
            str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
            r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
            r = r.json()
            dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output
            dic0 = dict_json['data']
            for k, v in dic0.items():
               if k == 'values':
                  if v != None:                         
                      df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                      df.insert(0, 'mkt-pair', l0[i])
                      df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                      df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                      print("Working on "+ str(i)+" :") #+ l2[i])
# # normalize(
#  l3 = df1[df1.pair.str.contains('USD')]['mkt-pair'].tolist()
#  len(l3)
#  l3.sort()   

def get_key(val):
    for key, value in my_dict.items():
         if val == value:
             return key 
    return "key doesn't exist"

#    json file block !!!!!!!!!!!!!!!!!!!!!  +++++++++++++++++++++++
d15 = "2020-12-12"
d16 = '2021-01-01'
for i in range(len(l0)):
    # if i > 10:
    #     pass
    # else: 
        r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d15+"T00:00:15.000Z&end="+d16+"T00:00:00.000Z&interval=15m", headers=headers)
        r = r.json()
        dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
        dic0 = dict_json['data']
        for k, v in dic0.items():
           if k == 'values':
               if v == None: 
                   pass
               else:        
                   outfile = open("D:\\infotrend\\all_json\\"+ l0[i]+"-"+d15+"-"+d16+".json", "w") 
                   json.dump(r, outfile) 
                   print("Working on "+ str(i))  #+" :" + l2[i])
     
        
############################################################################ single file pull     , dont edit!!!!!!!!!!!!!!!!!!!!!!   
newone ='poloniex-mdt-usdt'    #   -2020-12-12-2021-01-01
d11 = "2020-06-15"
d12 = "2020-07-05"  #-2020-08-14
d13 = "2020-07-25"
d14 = "2020-09-03"       
d15 = "2020-09-23"
d16 = '2020-10-13'
r = requests.get("https://data.messari.io/api/v1/markets/"+newone+"/metrics/price/time-series?beg="+d11+"T00:00:15.000Z&end="+d12+"T00:00:00.000Z&interval=15m", headers=headers)
r = r.json()
dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
dic0 = dict_json['data']
for k, v in dic0.items():
   if k == 'values':
       if v != None:               
          df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
          df.insert(0, 'mkt-pair', newone)  #l0[i])
          df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
          df.to_csv("D:\\infotrend\\master_csv\\"+newone+"-"+d11+'-'+d12+".csv", index=False)
          
######################################################################### DONT' EDIT #######################################
d15 = "2017-11-02"
d16 = '2017-11-23'
for i in range(len(l0)):
    # if i > 10:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d15+"T00:00:15.000Z&end="+d16+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
           if v != None: 
               if os.path.exists("D:\\infotrend\\master_json\\"+l0[i]+"-"+d15+"-"+d16+".json"):
                   break
               else:        
                   outfile = open("D:\\infotrend\\master_json\\"+l0[i]+"-"+d15+"-"+d16+".json", "w") 
                   json.dump(r, outfile) 
                   outfile.close()
                   print("Working on "+ str(i))  #+" :" + l2[i])
         
####################################################################################################################################
     
     
print(d13)
print(d15)        
     
d13 = "2020-11-22"
for i in range(len(l0)):
     r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d13+"T00:00:15.000Z&end="+d15+"T00:00:00.000Z&interval=15m", headers=headers)
     r = r.json()
     dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
     dic0 = dict_json['data']
     if dic0.get("values") == None:
        pass
     else:  
        outfile = open("D:\\infotrend\\all_json\\"+ l0[i]+"-"+d13+"-"+d15+".json", "w") 
        json.dump(r, outfile) 
      #  print("Working on "+ str(i))  #+" :" + l2[i])
          
                   
          
                           
          
### ====          #  csv block
           
          
for i in range(len(l0)):
     r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d13+"T00:00:15.000Z&end="+d15+"T00:00:00.000Z&interval=15m", headers=headers)
     r = r.json()
     dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
     dic0 = dict_json['data']
     if dic0.get("values") == None:
         pass
     else:          
          
                   
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d13+"T00:00:15.000Z&end="+d15+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
              df.insert(0, 'mkt-pair', l0[i])
              df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
              df.to_csv("D:\\infotrend\\all_json\\"+ l0[i]+"-"+d13+"-"+d15+".csv", index=False)
               # print("Working on "+ str(i)+" :") #+ l2[i])"
               
                     
d12 = "2020-11-02"
for i in range(len(l0)):
    # if i < 863:
    #     pass
    # else: 
        r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d12+"T00:00:15.000Z&end="+d13+"T00:00:00.000Z&interval=15m", headers=headers)
        r = r.json()
        dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
        dic0 = dict_json['data']
        for k, v in dic0.items():
           if k == 'values':
              if v == None: 
                  pass
              else:                         
                  df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                  df.insert(0, 'mkt-pair', l0[i])
                  df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                  df.to_csv("D:\\infotrend\\2020_15min_csv\\"+ l0[i]+"-"+d15+"-"+d16+".csv", index=False)
          #    time.sleep(1)#  "
d11 = "2020-10-13"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d11+"T00:00:15.000Z&end="+d12+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()  
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d11+"-"+d12+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
          #   time.sleep(1)#  "
d10 = "2020-09-23"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d10+"T00:00:15.000Z&end="+d11+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d10+"-"+d11+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
        #      time.sleep(1)#  "

#############################  dont edit!!!!!!!!!!!!!!
d9 = '2020-09-03'
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d9+"T00:00:15.000Z&end="+d10+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v != None:                               
         #     outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d9+"-"+d10+".json", "w") 
         #     json.dump(r, outfile) 
         #     print("Working on "+ str(i))  #+" :" + l2[i])
         # #    time.sleep(1)#  "
         
             df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
             df.insert(0, 'mkt-pair', l0[i])
             df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
             df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+d9+"-"+d10+".csv", index=False)
             print("Working on "+ str(i)+" :"+ l0[i])         
###############################################################################################################################################         
d8 = "2020-08-14"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d8+"T00:00:15.000Z&end="+d9+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
      
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d8+"-"+d9+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
          #    time.sleep(1)#  "
               
d7 = "2020-07-25"
for i in range(len(l0)):
     r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d7+"T00:00:15.000Z&end="+d8+"T00:00:00.000Z&interval=15m", headers=headers)
     r = r.json()
     dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
     dic0 = dict_json['data']
     for k, v in dic0.items():
        if k == 'values':
           if v == None: 
               pass
           else:                         
               outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d7+"-"+d8+".json", "w") 
               json.dump(r, outfile) 
               print("Working on "+ str(i))  #+" :" + l2[i])
          #     time.sleep(1)#  "D
              
d6 = "2020-07-05"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d6+"T00:00:15.000Z&end="+d7+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d6+"-"+d7+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
       #        time.sleep(1)#  "
               
d5 = "2020-06-15"   #  i = 207 , error below
# {"status":{"elapsed":2005,"timestamp":"2021-02-07T00:23:02.802338425Z","error_code":500,"error_message":"Internal Server Error"}}
#  https://data.messari.io:443 "GET /api/v1/markets/binance-btt-usdc/metrics/price/time-series?beg=2020-06-15T00:00:15.000Z&end=2020-07-05T00:00:00.000Z&interval=15m HTTP/1.1" 500 137
for i in range(len(l0)):
    # if i < 2104:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d5+"T00:00:15.000Z&end="+d6+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d5+"-"+d6+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
        #     time.sleep(1)#  "
                   
d4 = "2020-05-26"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d4+"T00:00:15.000Z&end="+d5+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d4+"-"+d5+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
           #   time.sleep(1)#  "
          
d3 = "2020-05-06"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d3+"T00:00:15.000Z&end="+d4+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d3+"-"+d4+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
       #      time.sleep(1)#  "
          
d2 = "2020-04-16"
for i in range(len(l0)):
    if i< 2030:
        pass
    else: 
        r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d2+"T00:00:15.000Z&end="+d3+"T00:00:00.000Z&interval=15m", headers=headers)
        r = r.json()
        dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
        dic0 = dict_json['data']
        for k, v in dic0.items():
           if k == 'values':
              if v == None: 
                  pass
              else:                         
                  outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d2+"-"+d3+".json", "w") 
                  json.dump(r, outfile) 
                  print("Working on "+ str(i))  #+" :" + l2[i])
                  time.sleep(1)
                       
d1 = "2020-03-27"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d1+"T00:00:15.000Z&end="+d2+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d1+"-"+d2+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
        #      time.sleep(1)#  "#  "
          
d14 = "2020-03-07"
for i in range(len(l0)):
    # if i< 784: 
    #     pass
    # else:
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d14+"T00:00:15.000Z&end="+d1+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d14+"-"+d1+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
         #     time.sleep(1)#  "
          
d17 = "2020-02-16"
for i in range(len(l0)):
    # if i < 1180:
    #     pass
    # else:
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d17+"T00:00:15.000Z&end="+d14+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d17+"-"+d14+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
         #     time.sleep(1)#  "
          
d18 = "2020-01-27"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d18+"T00:00:15.000Z&end="+d17+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d18+"-"+d17+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
        #      time.sleep(1)#  "
          
d19 = "2020-01-07"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d19+"T00:00:15.000Z&end="+d18+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d19+"-"+d18+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
         #     time.sleep(1)#  "
#  print(len(l0))     3168
         
print(l0.index("poloniex-nxt-ust"))

d20 = "2019-12-18"
d21 = "2019-11-27"
d22 = "2019-11-07"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d22+"T00:00:15.000Z&end="+d21+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d22+"-"+d21+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d23 = "2019-10-18"
for i in range(len(l0)):
    # if i< 3043:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d23+"T00:00:15.000Z&end="+d22+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d23+"-"+d22+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d24 = "2019-09-28"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d24+"T00:00:15.000Z&end="+d23+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d24+"-"+d23+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d25 = "2019-09-07"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d25+"T00:00:15.000Z&end="+d24+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d25+"-"+d24+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d26 = "2019-08-18"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d26+"T00:00:15.000Z&end="+d25+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d26+"-"+d25+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d27 = "2019-07-28"
for i in range(len(l0)):
    # if i < 2876:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d27+"T00:00:15.000Z&end="+d26+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d27+"-"+d26+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d28 = "2019-07-07"
for i in range(len(l0)):
    if i < 1742:
        pass
    else: 
        r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d28+"T00:00:15.000Z&end="+d27+"T00:00:00.000Z&interval=15m", headers=headers)
        r = r.json()
        dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
        dic0 = dict_json['data']
        for k, v in dic0.items():
           if k == 'values':
              if v == None: 
                  pass
              else:                         
                  outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d28+"-"+d27+".json", "w") 
                  json.dump(r, outfile) 
                  print("Working on "+ str(i))  #+" :" + l2[i])

d29 = "2019-06-16"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d29+"T00:00:15.000Z&end="+d28+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d29+"-"+d28+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d30 = "2019-05-26"
for i in range(len(l0)):
    # if i < 2194:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d30+"T00:00:15.000Z&end="+d29+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d30+"-"+d29+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
d31= "2019-05-05"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d31+"T00:00:15.000Z&end="+d30+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d31+"-"+d30+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
d32= "2019-04-14"
for i in range(len(l0)):
    if i < 1867:
        pass
    else: 
        r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d32+"T00:00:15.000Z&end="+d31+"T00:00:00.000Z&interval=15m", headers=headers)
        r = r.json()
        dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
        dic0 = dict_json['data']
        for k, v in dic0.items():
           if k == 'values':
              if v == None: 
                  pass
              else:                         
                  outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d32+"-"+d31+".json", "w") 
                  json.dump(r, outfile) 
                  print("Working on "+ str(i))  #+" :" + l2[i])
d33= "2019-03-24"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d33+"T00:00:15.000Z&end="+d32+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d33+"-"+d32+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])
d34= "2019-03-03"
for i in range(len(l0)):
    # if i < 1085:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d34+"T00:00:15.000Z&end="+d33+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d34+"-"+d33+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d35= "2019-02-10"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d35+"T00:00:15.000Z&end="+d34+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d35+"-"+d34+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d36= "2019-01-20"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d36+"T00:00:15.000Z&end="+d35+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d36+"-"+d35+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d37= "2018-12-30"
for i in range(len(l0)):
    # if i < 1085:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d37+"T00:00:15.000Z&end="+d36+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d37+"-"+d36+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d38= "2018-12-09"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d38+"T00:00:15.000Z&end="+d37+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d38+"-"+d37+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d39= "2018-11-18"
for i in range(len(l0)):
    # if i < 1085:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d39+"T00:00:15.000Z&end="+d38+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d39+"-"+d38+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i]

d40= "2018-10-28"
for i in range(len(l0)):
    # if i < 2947:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d40+"T00:00:15.000Z&end="+d39+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d40+"-"+d39+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i])

d41= "2018-10-07"
for i in range(len(l0)):
    # if i < 1085:
    #     pass
    # else: 
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d41+"T00:00:15.000Z&end="+d40+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d41+"-"+d40+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i]
d42= "2018-09-16"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d42+"T00:00:15.000Z&end="+d41+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d42+"-"+d41+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i]
d43= "2018-08-26"
for i in range(len(l0)):
    if i < 2292: 
        pass
    else: 
        r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d43+"T00:00:15.000Z&end="+d42+"T00:00:00.000Z&interval=15m", headers=headers)
        r = r.json()
        dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
        dic0 = dict_json['data']
        for k, v in dic0.items():
           if k == 'values':
              if v == None: 
                  pass
              else:                         
                  outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d43+"-"+d42+".json", "w") 
                  json.dump(r, outfile) 
                  print("Working on "+ str(i))  #+" :" + l2[i]              
d44= "2018-08-05"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d44+"T00:00:15.000Z&end="+d43+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d44+"-"+d43+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i]           
              d44= "2018-08-05"
d45= "2018-07-15"
for i in range(len(l0)):
    r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+d45+"T00:00:15.000Z&end="+d44+"T00:00:00.000Z&interval=15m", headers=headers)
    r = r.json()
    dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
    dic0 = dict_json['data']
    for k, v in dic0.items():
       if k == 'values':
          if v == None: 
              pass
          else:                         
              outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+d45+"-"+d44+".json", "w") 
              json.dump(r, outfile) 
              print("Working on "+ str(i))  #+" :" + l2[i]           
                           
# ================== below is for btc-usd      from 2011 -to 03/28/2013   #########   +++++++++++++++
str1_list = ["2011-10-20T00:00:15.000Z&end=2011-11-10", "2011-10-20T00:00:15.000Z&end=2011-11-10", "2011-11-10T00:00:15.000Z&end=2011-12-01",
"2011-12-01T00:00:15.000Z&end=2011-12-22", "2011-12-22T00:00:15.000Z&end=2012-01-12", "2012-01-12T00:00:15.000Z&end=2012-02-02",
"2012-02-02T00:00:15.000Z&end=2012-02-23", "2012-02-23T00:00:15.000Z&end=2012-03-15", "2012-03-15T00:00:15.000Z&end=2012-04-05",
"2012-04-05T00:00:15.000Z&end=2012-04-26", "2012-04-26T00:00:15.000Z&end=2012-05-17", "2012-05-17T00:00:15.000Z&end=2012-06-07",
"2012-06-07T00:00:15.000Z&end=2012-06-28", "2012-06-28T00:00:15.000Z&end=2012-07-19", "2012-07-19T00:00:15.000Z&end=2012-08-09",
"2012-08-09T00:00:15.000Z&end=2012-08-30", "2012-08-30T00:00:15.000Z&end=2012-09-20", "2012-09-20T00:00:15.000Z&end=2012-10-11",
"2012-10-11T00:00:15.000Z&end=2012-11-01", "2012-11-01T00:00:15.000Z&end=2012-11-22", "2012-11-22T00:00:15.000Z&end=2012-12-13",
"2012-12-13T00:00:15.000Z&end=2013-01-03", "2013-01-03T00:00:15.000Z&end=2013-01-24", "2013-01-24T00:00:15.000Z&end=2013-02-14",
"2013-02-14T00:00:15.000Z&end=2013-03-07", "2013-03-07T00:00:15.000Z&end=2013-03-28"]
for x in range(len(str1_list)):
    for i in range(len(l0)):
        if i != 1584:
            pass
        else:             
            str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
            r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
            r = r.json()
            dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
            dic0 = dict_json['data']
            for k, v in dic0.items():
               if k == 'values':
                  if v == None: 
                      pass
                  else:                         
                      outfile = open("D:\\infotrend\\2020_15min_json\\"+ l0[i]+"-"+str2+".json", "w") 
                      json.dump(r, outfile) 
                      print("Working on "+ str(i))  #+" :" + l2[i]   
print("Done!")                # btc-usd 1d interval starts at 2017-11-10
   ############  ==================================================================================
   
     
str1_list = ["2013-03-28T00:00:15.000Z&end=2013-04-18","2013-04-18T00:00:15.000Z&end=2013-05-09","2013-05-09T00:00:15.000Z&end=2013-05-30", "2013-05-30T00:00:15.000Z&end=2013-06-20"]
for x in range(len(str1_list)):     
    # if x <1:
    #     pass
    # else: 
        for i in range(len(l0)):    # if you change to l1, there's 3 places to change!!!
            # if i < 2846:
            #     pass
            # else:             
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r = r.json()
                dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
                dic0 = dict_json['data']
                for k, v in dic0.items():
                   if k == 'values':
                      if v == None: 
                          pass
                      else:                         
                          outfile = open("D:\\infotrend\\2020_15min_json\\"+l0[i]+"-"+str2+".json", "w") 
                          json.dump(r, outfile) 
                    #      time.sleep(0.001)



# str1_list = ["2013-06-20T00:00:15.000Z&end=2013-07-11"] #
# str1_list = ["2013-07-11T00:00:15.000Z&end=2013-08-01","2013-08-01T00:00:15.000Z&end=2013-08-22",
# "2013-08-22T00:00:15.000Z&end=2013-09-12","2013-09-12T00:00:15.000Z&end=2013-10-03","2013-10-03T00:00:15.000Z&end=2013-10-24","2013-10-24T00:00:15.000Z&end=2013-11-14",
# str1_list=["2013-11-14T00:00:15.000Z&end=2013-12-05"]
# str1_list=["2013-12-05T00:00:15.000Z&end=2013-12-26","2013-12-26T00:00:15.000Z&end=2014-01-16",    
   

str1_list = ["2014-01-16T00:00:15.000Z&end=2014-02-06"]   # needs to check if it's 15 files!!!!!!!!



# str1_list=  # ["2014-02-06T00:00:15.000Z&end=2014-02-27","2014-02-27T00:00:15.000Z&end=2014-03-20","2014-03-20T00:00:15.000Z&end=2014-04-10",
# str1_list =["2014-04-10T00:00:15.000Z&end=2014-05-01", "2014-05-01T00:00:15.000Z&end=2014-05-22",            
# str1_list = ["2014-05-22T00:00:15.000Z&end=2014-06-12"]
# ["2014-06-12T00:00:15.000Z&end=2014-07-03","2014-07-03T00:00:15.000Z&end=2014-07-24",
# str1_list = ["2014-07-24T00:00:15.000Z&end=2014-08-14"]
# str1_list = ["2014-08-14T00:00:15.000Z&end=2014-09-04"]
# ["2014-09-04T00:00:15.000Z&end=2014-09-25","2014-09-25T00:00:15.000Z&end=2014-10-16"]
# str1_list =["2014-10-16T00:00:15.000Z&end=2014-11-06",         
# str1_list = ["2014-11-06T00:00:15.000Z&end=2014-11-27"]
# str1_list = # ["2014-11-27T00:00:15.000Z&end=2014-12-18"]  
# str1_list =  ["2014-12-18T00:00:15.000Z&end=2015-01-08"]
# str1_list = ["2015-01-08T00:00:15.000Z&end=2015-01-29","2015-01-29T00:00:15.000Z&end=2015-02-19"]
# str1_list =["2015-02-19T00:00:15.000Z&end=2015-03-12","2015-03-12T00:00:15.000Z&end=2015-04-02"]
# # str1_list = ["2015-04-02T00:00:15.000Z&end=2015-04-23","2015-04-23T00:00:15.000Z&end=2015-05-14"]
# str1_list =["2015-05-14T00:00:15.000Z&end=2015-06-04","2015-06-04T00:00:15.000Z&end=2015-06-25"]
# str1_list = ["2015-06-25T00:00:15.000Z&end=2015-07-16","2015-07-16T00:00:15.000Z&end=2015-08-06","2015-08-06T00:00:15.000Z&end=2015-08-27","2015-08-27T00:00:15.000Z&end=2015-09-17"]
# str1_list = ["2015-09-17T00:00:15.000Z&end=2015-10-08","2015-10-08T00:00:15.000Z&end=2015-10-29","2015-10-29T00:00:15.000Z&end=2015-11-19","2015-11-19T00:00:15.000Z&end=2015-12-10", 
#              "2015-12-10T00:00:15.000Z&end=2015-12-31","2015-12-31T00:00:15.000Z&end=2016-01-21","2016-01-21T00:00:15.000Z&end=2016-02-11","2016-02-11T00:00:15.000Z&end=2016-03-03",      
#              "2016-03-03T00:00:15.000Z&end=2016-03-24","2016-03-24T00:00:15.000Z&end=2016-04-14","2016-04-14T00:00:15.000Z&end=2016-05-05","2016-05-05T00:00:15.000Z&end=2016-05-26"]
# str1_list = ["2016-05-26T00:00:15.000Z&end=2016-06-16","2016-06-16T00:00:15.000Z&end=2016-07-07", "2016-07-07T00:00:15.000Z&end=2016-07-28"       
# str1_list = ["2016-07-28T00:00:15.000Z&end=2016-08-18", "2016-08-18T00:00:15.000Z&end=2016-09-08","2016-09-08T00:00:15.000Z&end=2016-09-29","2016-09-29T00:00:15.000Z&end=2016-10-20","2016-10-20T00:00:15.000Z&end=2016-11-10", 
# "2016-11-10T00:00:15.000Z&end=2016-12-01","2016-12-01T00:00:15.000Z&end=2016-12-22","2016-12-22T00:00:15.000Z&end=2017-01-12","2017-01-12T00:00:15.000Z&end=2017-02-02",
# "2017-02-02T00:00:15.000Z&end=2017-02-23","2017-02-23T00:00:15.000Z&end=2017-03-16","2017-03-16T00:00:15.000Z&end=2017-04-06","2017-04-06T00:00:15.000Z&end=2017-04-27"]
str1_list = ["2017-06-08T00:00:15.000Z&end=2017-06-29"]
str1_list=["2016-07-28T00:00:15.000Z&end=2016-08-18"] 
str1_list = ["2016-08-18T00:00:15.000Z&end=2016-09-08","2016-09-08T00:00:15.000Z&end=2016-09-29","2016-09-29T00:00:15.000Z&end=2016-10-20",
"2016-10-20T00:00:15.000Z&end=2016-11-10","2016-11-10T00:00:15.000Z&end=2016-12-01","2016-12-01T00:00:15.000Z&end=2016-12-22","2016-12-22T00:00:15.000Z&end=2017-01-12",
"2017-01-12T00:00:15.000Z&end=2017-02-02","2017-02-02T00:00:15.000Z&end=2017-02-23","2017-02-23T00:00:15.000Z&end=2017-03-16","2017-03-16T00:00:15.000Z&end=2017-04-06",
"2017-04-06T00:00:15.000Z&end=2017-04-27","2017-04-27T00:00:15.000Z&end=2017-05-18","2017-05-18T00:00:15.000Z&end=2017-06-08"]
str1_list = ["2017-06-29T00:00:15.000Z&end=2017-07-20","2017-07-20T00:00:15.000Z&end=2017-08-10","2017-08-10T00:00:15.000Z&end=2017-08-31","2017-08-31T00:00:15.000Z&end=2017-09-21",
"2017-09-21T00:00:15.000Z&end=2017-10-12","2017-10-12T00:00:15.000Z&end=2017-11-02","2017-11-02T00:00:15.000Z&end=2017-11-23","2017-11-23T00:00:15.000Z&end=2017-12-14",
"2017-12-14T00:00:15.000Z&end=2018-01-04","2018-01-04T00:00:15.000Z&end=2018-01-25","2018-01-25T00:00:15.000Z&end=2018-02-15",
str1_list=["2018-02-15T00:00:15.000Z&end=2018-03-08"]   #,
str1_list = ["2018-03-08T00:00:15.000Z&end=2018-03-29","2018-03-29T00:00:15.000Z&end=2018-04-19"]        
str1_list = ["2018-04-19T00:00:15.000Z&end=2018-05-10", "2018-05-10T00:00:15.000Z&end=2018-05-31"]                    
str1_list = ["2018-05-31T00:00:15.000Z&end=2018-06-21"]
             

             
             
str1_list = ["2018-06-21T00:00:15.000Z&end=2018-07-12", "2018-07-12T00:00:15.000Z&end=2018-07-15"]     # !!!!!!!!!!!!!!
 # print(len(str1_list))        #  print in case,   105 blocks!!!

for x in range(len(str1_list)):     
    # if x <1:
    #     pass
    # else: 
        for i in range(len(l0)):    # if you change to l1, there's 3 places to change!!!
            if i < 2846:
                pass
            else:             
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r = r.json()
                dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
                dic0 = dict_json['data']
                for k, v in dic0.items():
                   if k == 'values':
                      if v == None: 
                          pass
                      else:                         
                          outfile = open("D:\\infotrend\\2020_15min_json\\"+l0[i]+"-"+str2+".json", "w") 
                          json.dump(r, outfile) 
                    #      time.sleep(0.001)
                        # print("Working on "+ str(i))  #+" :" + l2[i]   
print("Done!")     
print("--- It took %.3f seconds ---" % (time.time()-start_time))


###  ========================= for csv part below

str1_list = ["2021-01-01T00:00:15.000Z&end=2021-01-22"]
# str1_list = ["2021-01-01T00:00:15.000Z&end=2021-01-22"]

                          df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                          df.insert(0, 'mkt-pair', l0[i])
                          df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                          df.to_csv("D:\\infotrend\\2021_15min_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                          print("Working on "+ str(i)+" :") #+ l2[i])
                          time.sleep(0.02)#  "D




#  ==================================== if breaks

for x in range(len(str1_list)):      # current 05-01-05-22
 #   if x ==1:        
        for i in range(len(l0)):
            if i < 2846:
                pass
            else:             
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r = r.json()
                dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
                dic0 = dict_json['data']
                for k, v in dic0.items():
                   if k == 'values':
                      if v == None: 
                          pass
                      else:                         
                          outfile = open("D:\\infotrend\\2020_15min_json\\"+l0[i]+"-"+str2+".json", "w") 
                          json.dump(r, outfile) 
                          print("Working on "+ str(i))  #+" :" + l2[i]   
print("Done!")     









##################################################### return key, wrking!!!!!!
print(l0[1584])            #   bitstamp-btc-usd
   
hit = []   
z=0
str1_list = ["2013-03-31T00:00:15.000Z&end=2013-04-01"]                   # no result from above 3000
for x in range(len(str1_list)):      # current 05-01-05-22
    # 
 #   if x ==1:        
        for i in range(len(l0)):
            if i < 3000:
                pass
            else:             
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r = r.json()
                dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
                dic0 = dict_json['data']
                if dic0.get("values") == None:
                    pass
                else:                 
                    z += 1
                    hit.append(dic0.get("market_slug"))
with open("D:\\infotrend\\"+str2+"-.txt", 'w', newline='') as f:
    # fieldnames = ['count', 'slug']
    # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    f.write(str(hit))
                    #   f.write(dic0.get("market_slug"))          
                                               
##### ======================================================================================================================     
                    
    
hit = []      #  any single day, how many has values            
z=0
str1_list = ["2018-07-12T00:00:15.000Z&end=2018-07-13"]  #   ["2013-03-31T00:00:15.000Z&end=2013-04-01"]
for x in range(len(str1_list)):      # current 05-01-05-22
    # 
 #   if x ==1:        
        for i in range(len(l0)):
            # if i != 1584:# < 1585:  #< 3000:
            #     pass
            # else:             
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=1d", headers=headers)
                r = r.json()
                dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
                dic0 = dict_json['data']
                if dic0.get("values") == None:
                    pass
                else:                 
                    z += 1
                    hit.append(dic0.get("market_slug"))
print(z)
with open("D:\\infotrend\\"+str2+"-.txt", 'w', newline='') as f:
 # fieldnames = ['count', 'slug']
# #     # writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    f.write(str(hit))
# #                     #   f.write(dic0.get("market_slug"))   
                   
               
                
               
 #   =============              
                  
# file = open("D:\\infotrend\\"+str2+"-.txt", 'a+', newline ='') 
# # writing the data into the file 
# with file:     
#     write = csv.writer(file) 
#     write.writerows(hit)             
                   
                    
                   
                    
                    
                                  
                                  "title; post")
    f.write("\n")
                    
                    df = pd.DataFrame(dic0.get("market_slug")) #  dic0.values(), index=dic0.keys())
                    df.insert(0, 'count', )
                    
               #     print() 
               
               
               
               #alues())  #[0])  #0.keys())  # values())  #[2]) #   z+=1
                    with open("D:\\infotrend\\"+str2+"-sum2.txt", 'w') as file:
                                file.write(z)  # r(         
                      #     print(v)
              #             hit.append([v for v in dic0.values()[:3]])
                           
                           
  #                          df_p = pd.DataFrame(dic0)
  # #  df_p = df_p[['pair']] df_p.to 
  #                    #      if k == 'market_slug':
  #                          hit.append(k == 'market_slug')
                           z))
                  #              file.write(str(hit))#, hit)   #str(len(hit)))
                                                    
                           
print(len(hit))                    
                           
                            
                           
                            
################### =========================================================================================
z=0
str1_list = ["2013-03-31T00:00:15.000Z&end=2013-04-01"]
for x in range(len(str1_list)):      # current 05-01-05-22
 #   if x ==1:        
        for i in range(len(l0)):
            # if i!=1584:
            #     pass
            # else:             
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r = r.json()
                dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output.
                dic0 = dict_json['data']
                for k, v in dic0.items():
                    if k == 'values':
                        if v == None: 
                           pass
                        else:
                           z+=1
                           hit.append([v for v in dic0.values()[:3]])
                           
                           
  #                          df_p = pd.DataFrame(dic0)
  # #  df_p = df_p[['pair']] df_p.to 
  #                    #      if k == 'market_slug':
  #                          hit.append(k == 'market_slug')
                           with open("D:\\infotrend\\"+str2+"-sum2.txt", 'w') as file:
                                file.write(str(z))
                                file.write(str(hit))#, hit)   #str(len(hit)))                         
                            
                           
                            
                            
                           
                            fout = "D:\\infotrend\\"+str2+"-sum.txt"
                            fo = open(fout, "w")

                            for k, v in dic0.items():
                                fo.write(str(k) + ' >>> '+ str(v) + '\n\n')
                                fo.close()
                           
                     #       df = pd.DataFrame()  #k.values())      #  , columns = t'])  # , 'high', 'low', 'close', 'volume'])
                     #       df.insert(0, 'count', len(hit))  #])
                     # #     df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                     #       df.to_csv("D:\\infotrend\\"+str2+"-sum.csv", index=False)
                     #      # print("Working on "+ str(i)+" :") #+ l2[i])
                     #      # time.sleep(0.02)#  "
             
                    
                        
             
                    
                  
                    # else:    
                   #     break
                   #    print(k)   for 2 in k:
                   #        print(k[2])   #.items())   #get("market_slug"))    #     ##    for k1, v1 in k:  #[0])
                   #      print(k1, v1)
                       
                   #     hit.append(k[2])  #=="market_slug")   # outfile = open("D:\\infotrend\\2020_15min_json\\"+l0[i]+"-"+str2+".json", "w") 
                          # json.dump(r, outfile) 
print(len(hit)) 
print(hit)   #k=="market_slug")  "v)  # Working on "+ str(i))  #+" :" + l2[i]   
                          
                          
                          
                          
############=============================== btc =========   dont' edit =================================
str1_list = ["2011-08-18T00:00:15.000Z&end=2011-09-08", "2011-09-08T00:00:15.000Z&end=2011-09-29", "2011-09-29T00:00:15.000Z&end=2011-10-20",
"2011-10-20T00:00:15.000Z&end=2011-11-10", "2011-11-10T00:00:15.000Z&end=2011-12-01", "2011-12-01T00:00:15.000Z&end=2011-12-22", 
"2011-12-22T00:00:15.000Z&end=2012-01-12", "2012-01-12T00:00:15.000Z&end=2012-02-02", "2012-02-02T00:00:15.000Z&end=2012-02-23",
"2012-02-23T00:00:15.000Z&end=2012-03-15", "2012-03-15T00:00:15.000Z&end=2012-04-05",
"2012-04-05T00:00:15.000Z&end=2012-04-26", "2012-04-26T00:00:15.000Z&end=2012-05-17", "2012-05-17T00:00:15.000Z&end=2012-06-07",
"2012-06-07T00:00:15.000Z&end=2012-06-28", "2012-06-28T00:00:15.000Z&end=2012-07-19", "2012-07-19T00:00:15.000Z&end=2012-08-09",
"2012-08-09T00:00:15.000Z&end=2012-08-30", "2012-08-30T00:00:15.000Z&end=2012-09-20", "2012-09-20T00:00:15.000Z&end=2012-10-11",
"2012-10-11T00:00:15.000Z&end=2012-11-01", "2012-11-01T00:00:15.000Z&end=2012-11-22", "2012-11-22T00:00:15.000Z&end=2012-12-13",
"2012-12-13T00:00:15.000Z&end=2013-01-03", "2013-01-03T00:00:15.000Z&end=2013-01-24",
"2013-01-24T00:00:15.000Z&end=2013-02-14", "2013-02-14T00:00:15.000Z&end=2013-03-07", "2013-03-07T00:00:15.000Z&end=2013-03-28"]

for x in range(len(str1_list)):      #  json or  csv block!
    for i in range(len(l0)):  
        if i !=1584: # 1361:
            pass
        else: 
            str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
            r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
            r = r.json()
            dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output
            dic0 = dict_json['data']
            for k, v in dic0.items():
               if k == 'values':
                  if v == None: 
                      pass
                  else:    
                      outfile = open("D:\\infotrend\\2011_15min_json\\"+ l0[i]+"-"+str2+".json", "w") 
                      json.dump(r, outfile)     
                      
             
                      
                      df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                      df.insert(0, 'mkt-pair', l0[i])
                      df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                      df.to_csv("D:\\infotrend\\2011_15min_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                      print("Working on "+ str(i)+" :") #+ l2[i])


#################################################### ====== dont edit ================== 
print(l0[1161])  

str1_list = ["2016-12-01T00:00:15.000Z&end=2016-12-22"]  #", "2013-04-18T00:00:15.000Z&end=2013-05-09"]
for x in range(len(str1_list)):      #   csv for the only2
    for i in range(len(l0)):  
      #   if i !=1161: # or i!=1584:    #61: # 1361:
       if i <1457:   #or 1584:  
            pass
       else: 
            str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
            r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
            r = r.json()
            dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output
            dic0 = dict_json['data']
            for k, v in dic0.items():
               if k == 'values':
                  if v != None: 
                      if os.path.exists("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv"):
                          break
                      else:                                  
                          df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                          df.insert(0, 'mkt-pair', l0[i])
                          df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                          df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                          print("Working on "+ str(i)+" :") #+ l2[i])

#######################################################################################################
 # has not run csv  
str1_list = ["2015-12-31T00:00:15.000Z&end=2016-01-21"]     #  , "2013-05-30T00:00:15.000Z&end=2013-06-20", 
"2013-06-20T00:00:15.000Z&end=2013-07-11", "2013-07-11T00:00:15.000Z&end=2013-08-01", "2013-08-01T00:00:15.000Z&end=2013-08-22", 
"2013-08-22T00:00:15.000Z&end=2013-09-12", "2013-09-12T00:00:15.000Z&end=2013-10-03",
"2013-10-03T00:00:15.000Z&end=2013-10-24", "2013-10-24T00:00:15.000Z&end=2013-11-14", "2013-11-14T00:00:15.000Z&end=2013-12-05", "2013-12-05T00:00:15.000Z&end=2013-12-26",
"2013-12-26T00:00:15.000Z&end=2014-01-16", "2014-01-16T00:00:15.000Z&end=2014-02-06", "2014-02-06T00:00:15.000Z&end=2014-02-27",
"2014-02-27T00:00:15.000Z&end=2014-03-20", "2014-03-20T00:00:15.000Z&end=2014-04-10", "2014-04-10T00:00:15.000Z&end=2014-05-01",
"2014-05-01T00:00:15.000Z&end=2014-05-22", "2014-05-22T00:00:15.000Z&end=2014-06-12", "2014-06-12T00:00:15.000Z&end=2014-07-03",
"2014-07-03T00:00:15.000Z&end=2014-07-24", "2014-07-24T00:00:15.000Z&end=2014-08-14", "2014-08-14T00:00:15.000Z&end=2014-09-04",
"2014-09-04T00:00:15.000Z&end=2014-09-25", "2014-09-25T00:00:15.000Z&end=2014-10-16", "2014-10-16T00:00:15.000Z&end=2014-11-06",
"2014-11-06T00:00:15.000Z&end=2014-11-27", "2014-11-27T00:00:15.000Z&end=2014-12-18", "2014-12-18T00:00:15.000Z&end=2015-01-08",
"2015-01-08T00:00:15.000Z&end=2015-01-29", "2015-01-29T00:00:15.000Z&end=2015-02-19", "2015-02-19T00:00:15.000Z&end=2015-03-12",
"2015-03-12T00:00:15.000Z&end=2015-04-02", "2015-04-02T00:00:15.000Z&end=2015-04-23", "2015-04-23T00:00:15.000Z&end=2015-05-14",
"2015-05-14T00:00:15.000Z&end=2015-06-04", "2015-06-04T00:00:15.000Z&end=2015-06-25", "2015-06-25T00:00:15.000Z&end=2015-07-16",
"2015-07-16T00:00:15.000Z&end=2015-08-06", "2015-08-06T00:00:15.000Z&end=2015-08-27", "2015-08-27T00:00:15.000Z&end=2015-09-17",
"2015-09-17T00:00:15.000Z&end=2015-10-08", "2015-10-08T00:00:15.000Z&end=2015-10-29", "2015-10-29T00:00:15.000Z&end=2015-11-19",
"2015-11-19T00:00:15.000Z&end=2015-12-10", "2015-12-10T00:00:15.000Z&end=2015-12-31", "2015-12-31T00:00:15.000Z&end=2016-01-21",
"2016-01-21T00:00:15.000Z&end=2016-02-11", "2016-02-11T00:00:15.000Z&end=2016-03-03", "2016-03-03T00:00:15.000Z&end=2016-03-24",
"2016-03-24T00:00:15.000Z&end=2016-04-14", "2016-04-14T00:00:15.000Z&end=2016-05-05", "2016-05-05T00:00:15.000Z&end=2016-05-26",
"2016-05-26T00:00:15.000Z&end=2016-06-16", "2016-06-16T00:00:15.000Z&end=2016-07-07", "2016-07-07T00:00:15.000Z&end=2016-07-28",
"2016-07-28T00:00:15.000Z&end=2016-08-18", "2016-08-18T00:00:15.000Z&end=2016-09-08", "2016-09-08T00:00:15.000Z&end=2016-09-29",
"2016-09-29T00:00:15.000Z&end=2016-10-20", "2016-10-20T00:00:15.000Z&end=2016-11-10", "2016-11-10T00:00:15.000Z&end=2016-12-01",
"2016-12-01T00:00:15.000Z&end=2016-12-22", "2016-12-22T00:00:15.000Z&end=2017-01-12", "2017-01-12T00:00:15.000Z&end=2017-02-02",
"2017-02-02T00:00:15.000Z&end=2017-02-23", "2017-02-23T00:00:15.000Z&end=2017-03-16", "2017-03-16T00:00:15.000Z&end=2017-04-06",
"2017-04-06T00:00:15.000Z&end=2017-04-27", "2017-04-27T00:00:15.000Z&end=2017-05-18", "2017-05-18T00:00:15.000Z&end=2017-06-08",
"2017-06-08T00:00:15.000Z&end=2017-06-29", "2017-06-29T00:00:15.000Z&end=2017-07-20", "2017-07-20T00:00:15.000Z&end=2017-08-10",
"2017-08-10T00:00:15.000Z&end=2017-08-31", "2017-08-31T00:00:15.000Z&end=2017-09-21", "2017-09-21T00:00:15.000Z&end=2017-10-12",
"2017-10-12T00:00:15.000Z&end=2017-11-02", "2017-11-02T00:00:15.000Z&end=2017-11-23", "2017-11-23T00:00:15.000Z&end=2017-12-14",
"2017-12-14T00:00:15.000Z&end=2018-01-04", "2018-01-04T00:00:15.000Z&end=2018-01-25", "2018-01-25T00:00:15.000Z&end=2018-02-15",
"2018-02-15T00:00:15.000Z&end=2018-03-08", "2018-03-08T00:00:15.000Z&end=2018-03-29", "2018-03-29T00:00:15.000Z&end=2018-04-19",
"2018-04-19T00:00:15.000Z&end=2018-05-10", "2018-05-10T00:00:15.000Z&end=2018-05-31", "2018-05-31T00:00:15.000Z&end=2018-06-21",
"2018-06-21T00:00:15.000Z&end=2018-07-12", "2018-07-12T00:00:15.000Z&end=2018-07-15"]    
str1_list = ["2013-11-14T00:00:15.000Z&end=2013-12-05"]        #  is  1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735                                            
str1_list = ["2014-02-06T00:00:15.000Z&end=2014-02-27"]           #  + 2934, 2983, 3006, 3033, 3035, 3040, 3127, 3147
str1_list =["2014-02-27T00:00:15.000Z&end=2014-03-20", "2014-03-20T00:00:15.000Z&end=2014-04-10",
str1_list = ["2020-10-13T00:00:15.000Z&end=2020-11-02", "2015-07-16T00:00:15.000Z&end=2015-08-06", "2015-08-06T00:00:15.000Z&end=2015-08-27", "2015-08-27T00:00:15.000Z&end=2015-09-17",
"2015-09-17T00:00:15.000Z&end=2015-10-08", "2015-10-08T00:00:15.000Z&end=2015-10-29"] 



str1_list =["2016-12-22T00:00:15.000Z&end=2017-01-12", "2017-01-12T00:00:15.000Z&end=2017-02-02",
"2017-02-02T00:00:15.000Z&end=2017-02-23", "2017-02-23T00:00:15.000Z&end=2017-03-16", "2017-03-16T00:00:15.000Z&end=2017-04-06", "2017-04-06T00:00:15.000Z&end=2017-04-27"]

  
  

print(str1_list)
#  unrun csv block  some above
print(l0[2735]) 
print(l0[1139])     #  bitfinex-bfx-btc
###########################################################################   main, dont edit !!!!!! it writes lots of sum files but if it breaks you know where
for x in range(len(str1_list)):
 #   if x <1:             
        z=0
        els=[]
        for i in range(len(l0)): # [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735, 2934, 2983, 3006, 3033, 3035, 3040, 3127, 3147]:   #  range(len(l0)):  # #  [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735]:
      #       if i != 1584:  #1161:  #1325:  #1161:  #1584:       #   Working on 1161 :# Working on 1325 :# Working on 1326 :# Working on 1584 :
            # if i < 1161:  #3158:     #  611:   #2900:  #646: #1284:  #610:  #988:  #1320:  #9:  #1352: #618:  #05:  #39:  #2551:  #1604:  #35:  #324: 877: #161:   #580:  #9:   #784:  #1584:  #1162:  # 1584:  #3066:  #1585: # 2909:  #=2735:  #1161:  #1326:  #1584: #2735    1798:
            #     pass
            # else: 
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r=r.json()   #clean_result(r)  #r = r.json()
                dict_json=json.loads(json.dumps(r))    
                dic0 = dict_json['data']
                for k, v in dic0.items():
                   if k == 'values':
                      if v != None: 
                         try: 
                              df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                              df.insert(0, 'mkt-pair', l0[i])
                              df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                              df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                              z+=1  # l2[i])
                              els.append(l0[i])
                              print("Working on "+str(i)+": " + l0[i]) 
                              time.sleep(0.01)
                         except json.decoder.JSONDecodeError as e:    
                              print(e)
                              time.sleep(3)
                              print(l0[i]+ "didn't go through") 
                              continue #Total is :" + str(z)+ " files.")  
                         finally: 
                              with open('D:\\infotrend\\count\\sum-'+str2+'.csv', 'w') as f:
                                 for listitem in els:
                                    f.write('%s\n' % listitem)
                              #   f.write("Total is :"+str(z)+" files.")
                                 f.close()
           
print(" ~~~ Done!!!")                                        
              
#########################################################################   count, dont edit !!!!!!!!!!!!!  ##########
str1_list =  ["2019-05-26T00:00:15.000Z&end=2019-06-16"]    
for x in range(len(str1_list)):
        z=0
        els=[]
        for i in range(len(l0)): # [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735, 2934, 2983, 3006, 3033, 3035, 3040, 3127, 3147]:   #  range(len(l0)):  # #  [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735]:
      #       if i != 1584:  #1161:  #1325:  #1161:  #1584:       #   Working on 1161 :# Working on 1325 :# Working on 1326 :# Working on 1584 :
            # if i < 1161:  #3158:     #  611:   #2900:  #646: #1284:  #610:  #988:  #1320:  #9:  #1352: #618:  #05:  #39:  #2551:  #1604:  #35:  #324: 877: #161:   #580:  #9:   #784:  #1584:  #1162:  # 1584:  #3066:  #1585: # 2909:  #=2735:  #1161:  #1326:  #1584: #2735    1798:
            #     pass
            # else: 
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r=r.json()   #clean_result(r)  #r = r.json()
                dict_json=json.loads(json.dumps(r))     
                dic0 = dict_json['data']
                for k, v in dic0.items():
                   if k == 'values':
                      if v != None: 
                         try: 
                              # df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                              # df.insert(0, 'mkt-pair', l0[i])
                              # df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                              # df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                              z+=1  # l2[i])
                              els.append(l0[i])
                              print("Working on "+str(i)+": " + l0[i]) 
                              time.sleep(0.01)
                         except json.decoder.JSONDecodeError as e:    
                              print(e)
                              time.sleep(3)
                              print(l0[i]+ "didn't go through") 
                              continue #Total is :" + str(z)+ " files.")  
                         #finally: 
                  with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
                      for listitem in els:
                         f.write('%s\n' % listitem)
        #           print("Total is :"+str(z)+" files.")
                  f.close()           
print(" ~~~ Done!!!")   
#################################################################################### check if file exists   
str1_list = ["2017-06-08T00:00:15.000Z&end=2017-06-29","2017-06-29T00:00:15.000Z&end=2017-07-20","2017-07-20T00:00:15.000Z&end=2017-08-10"]

for x in range(len(str1_list)):
 #  if x < 4:
      # z=0
        # els=[]
        for i in range(len(l0)): # [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735, 2934, 2983, 3006, 3033, 3035, 3040, 3127, 3147]:   #  range(len(l0)):  # #  [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735]:
           #  if i != 1584:  #1161:  #1325:  #1161:  #1584:       #   Working on 1161 :# Working on 1325 :# Working on 1326 :# Working on 1584 :
            # if i <1431:  #3158:     #  611:   #2900:  #646: #1284:  #610:  #988:  #1320:  #9:  #1352: #618:  #05:  #39:  #2551:  #1604:  #35:  #324: 877: #161:   #580:  #9:   #784:  #1584:  #1162:  # 1584:  #3066:  #1585: # 2909:  #=2735:  #1161:  #1326:  #1584: #2735    1798:
            #     pass
            # else:
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r=r.json()   #clean_result(r)  #r = r.json()
                dict_json=json.loads(json.dumps(r))     
                dic0 = dict_json['data']
                
                for k, v in dic0.items():
                   if k == 'values':
                      if v != None: 
                         try: 
                             # df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                             # df.insert(0, 'mkt-pair', l0[i])
                             # df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                             # df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                               if os.path.exists("D:\\infotrend\\master_json\\"+l0[i]+"-"+str2+".json"):
                                   break
                               else: 
                                   outfile = open("D:\\infotrend\\master_json\\"+l0[i]+"-"+str2+".json", "w") 
                                   json.dump(r, outfile) 
                                   outfile.close()     
                                   print("Working on "+str(i)+": " + l0[i]) 
                    #           time.sleep(0.01)
                         except json.decoder.JSONDecodeError as e:    
                              print(e)
                              time.sleep(3)
                              print(l0[i]+ "didn't go through") 
                              continue #Total is :" + str(z)+ " files.")  
                   #     finally: 
                   #            with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
                   #               for listitem in els:
                   #                  f.write('%s\n' % listitem)
                   # #          print("Total is :"+str(z)+" files.")
                   #            f.close()           
print(" ~~~ Done!!!")   

# print(els)
# path.exists("guru99.txt")

#######################################################  testing...,file write should be same indent as for loop 
str1_list = ["2017-11-02T00:00:15.000Z&end=2017-11-23"]
for x in range(len(str1_list)):
 #   if x <1:             
    z=0
    els=[]
    for i in range(len(l0)): 
        try: 
             # [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735, 2934, 2983, 3006, 3033, 3035, 3040, 3127, 3147]:   #  range(len(l0)):  # #  [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735]:
          #   if i != 1584:  #1161:  #1325:  #1161:  #1584:       #   Working on 1161 :# Working on 1325 :# Working on 1326 :# Working on 1584 :
            # if i < 1129:  #3158:     #  611:   #2900:  #646: #1284:  #610:  #988:  #1320:  #9:  #1352: #618:  #05:  #39:  #2551:  #1604:  #35:  #324: 877: #161:   #580:  #9:   #784:  #1584:  #1162:  # 1584:  #3066:  #1585: # 2909:  #=2735:  #1161:  #1326:  #1584: #2735    1798:
            #     pass
            # else: 
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r=r.json()   #clean_result(r)  #r = r.json()
                dict_json=json.loads(json.dumps(r))    
                dic0 = dict_json['data']
                for k, v in dic0.items():
                    if k == 'values':
                        if v != None: 
                        
                            df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                            df.insert(0, 'mkt-pair', l0[i])
                            df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                            df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                            z+=1  # l2[i])
                            els.append(l0[i])
                              # outfile = open("D:\\infotrend\\master_json\\"+l0[i]+"-"+str2+".json", "w") 
                              # json.dump(r, outfile) 
                              # outfile.close()     
                            print("Working on "+str(i)+": " + l0[i]) 
           #               time.sleep(0.01)
        except json.decoder.JSONDecodeError as e:    
            print(e)
            time.sleep(3)
            print(l0[i]+ "didn't go through") 
            continue #Total is :" + str(z)+ " files.")  
        #             #     finally: 
            # with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
            #     for listitem in els:
            #         f.write('%s\n' % listitem)
            # #   f.write("Total is :"+str(z)+" files.")
            #     f.close()
           
print(" ~~~ Done!!!")   


##################################### gettin list error 
for x in range(len(str1_list)):
 #   if x <1:             
        z=0
        els=[]
        for i in range(len(l0)): # [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735, 2934, 2983, 3006, 3033, 3035, 3040, 3127, 3147]:   #  range(len(l0)):  # #  [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735]:
      #       if i != 1584:  #1161:  #1325:  #1161:  #1584:       #   Working on 1161 :# Working on 1325 :# Working on 1326 :# Working on 1584 :
            # if i < 1161:  #3158:     #  611:   #2900:  #646: #1284:  #610:  #988:  #1320:  #9:  #1352: #618:  #05:  #39:  #2551:  #1604:  #35:  #324: 877: #161:   #580:  #9:   #784:  #1584:  #1162:  # 1584:  #3066:  #1585: # 2909:  #=2735:  #1161:  #1326:  #1584: #2735    1798:
            #     pass
            # else: 
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r=r.json()   #clean_result(r)  #r = r.json()
                dict_json=json.loads(json.dumps(r))    
                dic0 = dict_json['data']
                for k, v in dic0.items():
                   if k == 'values':
                      if v != None: 
                         try: 
                              df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                              df.insert(0, 'mkt-pair', l0[i])
                              df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                              df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                              z+=1  # l2[i])
                              els.append(l0[i])
                              print("Working on "+str(i)+": " + l0[i]) 
                              time.sleep(0.01)
                         except json.decoder.JSONDecodeError as e:    
                              print(e)
                              time.sleep(3)
                              print(l0[i]+ "didn't go through") 
                              continue #Total is :" + str(z)+ " files.")  
                        # finally: 
                with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
                   for listitem in els:
                       f.write('%s\n' % listitem)
                    #   f.write("Total is :"+str(z)+" files.")
                   f.close()
           
print(" ~~~ Done!!!")                             


################################################################# USD !!!!!!!!!!!!!!!!!!!!!
str1_list = ["2020-03-07T00:00:15.000Z&end=2020-03-27", 
"2020-03-27T00:00:15.000Z&end=2020-04-16", "2020-04-16T00:00:15.000Z&end=2020-05-06", "2020-05-06T00:00:15.000Z&end=2020-05-26", "2020-05-26T00:00:15.000Z&end=2020-06-15",
"2020-06-15T00:00:15.000Z&end=2020-07-05", "2020-07-05T00:00:15.000Z&end=2020-07-25", "2020-07-25T00:00:15.000Z&end=2020-08-14", "2020-08-14T00:00:15.000Z&end=2020-09-03", 
"2020-09-03T00:00:15.000Z&end=2020-09-23", "2020-09-23T00:00:15.000Z&end=2020-10-13", "2020-10-13T00:00:15.000Z&end=2020-11-02", "2020-11-02T00:00:15.000Z&end=2020-11-22", 
"2020-11-22T00:00:15.000Z&end=2020-12-12", "2020-12-12T00:00:15.000Z&end=2021-01-01", "2020-01-01T00:00:15.000Z&end=2021-01-22"]

for x in range(len(str1_list)):
    try: # if x <1:             
     #
        for i in range(len(l0)): # [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735, 2934, 2983, 3006, 3033, 3035, 3040, 3127, 3147]:   #  range(len(l0)):  # #  [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735]:
            # if i < 2584:  #1161:  #1325:  #1161:  #1584:       #   Working on 1161 :# Working on 1325 :# Working on 1326 :# Working on 1584 :
            # # if i != 3163:  #3158:     #  611:   #2900:  #646: #1284:  #610:  #988:  #1320:  #9:  #1352: #618:  #05:  #39:  #2551:  #1604:  #35:  #324: 877: #161:   #580:  #9:   #784:  #1584:  #1162:  # 1584:  #3066:  #1585: # 2909:  #=2735:  #1161:  #1326:  #1584: #2735    1798:
            #     pass
            # else: 
                str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price.usd/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r=r.json()   #clean_result(r)  #r = r.json()
                dict_json=json.loads(json.dumps(r))    
                dic0 = dict_json['data']
                for k, v in dic0.items():
                   if k == 'values':
                      if v != None: 
                        # try: 
                              df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'price'])
              #                df.insert(0, 'mkt-pair', l0[i])
              #                df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                              df.to_csv("D:\\infotrend\\usd_csv\\"+l0[i]+"-"+str2+"-usd.csv", index=False)
                           #els.append(l0[i])
                              print("Working on "+str(i)+": " + l0[i]) 
                              time.sleep(2) 
    except json.decoder.JSONDecodeError as e:    
        print(e)
        time.sleep(3)
        print(l0[i]+ "didn't go through") 
        continue #Total is :" + str(z)+ " files.")  
















 ["2020-07-25T00:00:15.000Z&end=2020-08-14", "2019-05-05T00:00:15.000Z&end=2019-05-26", "2019-05-26T00:00:15.000Z&end=2019-06-16", "2019-06-16T00:00:15.000Z&end=2019-07-07", 
"2019-07-07T00:00:15.000Z&end=2019-07-28", "2019-07-28T00:00:15.000Z&end=2019-08-18", "2019-08-18T00:00:15.000Z&end=2019-09-07",
"2019-09-07T00:00:15.000Z&end=2019-09-28","2019-09-28T00:00:15.000Z&end=2019-10-18",
"2019-10-18T00:00:15.000Z&end=2019-11-07","2019-11-07T00:00:15.000Z&end=2019-11-27","2019-11-27T00:00:15.000Z&end=2019-12-18","2019-12-18T00:00:15.000Z&end=2020-01-07",
"2020-01-07T00:00:15.000Z&end=2020-01-27","2020-01-27T00:00:15.000Z&end=2020-02-16","2020-02-16T00:00:15.000Z&end=2020-03-07",
"2020-03-07T00:00:15.000Z&end=2020-03-27","2020-03-27T00:00:15.000Z&end=2020-04-16","2020-04-16T00:00:15.000Z&end=2020-05-06","2020-05-06T00:00:15.000Z&end=2020-05-26"]











"2020-09-03T00:00:15.000Z&end=2020-09-23","2020-09-23T00:00:15.000Z&end=2020-10-13",
"2020-10-13T00:00:15.000Z&end=2020-11-02","2020-11-02T00:00:15.000Z&end=2020-11-22","2020-11-22T00:00:15.000Z&end=2020-12-12","2020-12-12T00:00:15.000Z&end=2021-01-01"]

# z=0
# els=[]
    
# print(z)
for x in range(len(str1_list)):
    
    # if x <4:   # do not remove 
    
    for i in range(len(l0)):
        z=0
        els=[]
       
           # [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735, 2934, 2983, 3006, 3033, 3035, 3040, 3127, 3147]:   #  range(len(l0)):  # #  [1161, 1325, 1326, 1584, 2138, 2618, 2621, 2732, 2735]:
    # #       if i != 1584:  #1161:  #1325:  #1161:  #1584:       #   Working on 1161 :# Working on 1325 :# Working on 1326 :# Working on 1584 :
        if i < 3140:  #3158:     #  611:   #2900:  #646: #1284:  #610:  #988:  #1320:  #9:  #1352: #618:  #05:  #39:  #2551:  #1604:  #35:  #324: 877: #161:   #580:  #9:   #784:  #1584:  #1162:  # 1584:  #3066:  #1585: # 2909:  #=2735:  #1161:  #1326:  #1584: #2735    1798:
            pass
        else: 
            str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
            r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
            r=r.json()   #clean_result(r)  #r = r.json()
            dict_json=json.loads(json.dumps(r))
           
                 # json.loads take a string as input and returns a dictionary as output
            dic0 = dict_json['data']
            for k, v in dic0.items():
                if k == 'values':
                     if v != None: 
                         try:         
                                 # df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                                 # df.insert(0, 'mkt-pair', l0[i])
                                 # df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                                 # df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                               z+=1  # l2[i])
                               els.append(l0[i])
                               print("Working on "+str(i)+": " + l0[i]) 
                                 # time.sleep(0.1)
                         except json.decoder.JSONDecodeError as e:    
                               print(e)
                               time.sleep(0.3)
                               print(l0[i]+ "didn't go through") 
                               continue #Total is :" + str(z)+ " files.")  
                         finally: 
                               with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
                                   for listitem in els:
                                      f.write('%s\n' % listitem)
                            #       f.write("Total is :"+str(z)+" files.")
                                   f.close()
                    # else:
                    #     pa
                    
           
print(els)  # ~~~ Done!!!")
                 
    


## unrun below

"2018-01-04T00:00:15.000Z&end=2018-01-25", "2018-01-25T00:00:15.000Z&end=2018-02-15","2018-02-15T00:00:15.000Z&end=2018-03-08", 
"2018-03-08T00:00:15.000Z&end=2018-03-29", "2018-03-29T00:00:15.000Z&end=2018-04-19", "2018-04-19T00:00:15.000Z&end=2018-05-10", "2018-05-10T00:00:15.000Z&end=2018-05-31",
"2018-05-31T00:00:15.000Z&end=2018-06-21", "2018-06-21T00:00:15.000Z&end=2018-07-12", "2018-07-12T00:00:15.000Z&end=2018-07-15", "2018-07-15T00:00:15.000Z&end=2018-08-05", 
"2018-08-05T00:00:15.000Z&end=2018-08-26", "2018-08-26T00:00:15.000Z&end=2018-09-16","2018-09-16T00:00:15.000Z&end=2018-10-07", "2018-10-07T00:00:15.000Z&end=2018-10-28", 
"2018-10-28T00:00:15.000Z&end=2018-11-18", "2018-11-18T00:00:15.000Z&end=2018-12-09", "2018-12-09T00:00:15.000Z&end=2018-12-30", "2018-12-30T00:00:15.000Z&end=2019-01-20", 
"2019-01-20T00:00:15.000Z&end=2019-02-10",


            "2011-08-18T00:00:15.000Z&end=2011-09-08"
"2011-09-08T00:00:15.000Z&end=2011-09-29"
"2011-09-29T00:00:15.000Z&end=2011-10-20"
"2011-10-20T00:00:15.000Z&end=2011-11-10"
"2011-11-10T00:00:15.000Z&end=2011-12-01"
"2011-12-01T00:00:15.000Z&end=2011-12-22"
"2011-12-22T00:00:15.000Z&end=2012-01-12"
"2012-01-12T00:00:15.000Z&end=2012-02-02"
"2012-02-02T00:00:15.000Z&end=2012-02-23"
"2012-02-23T00:00:15.000Z&end=2012-03-15"
"2012-03-15T00:00:15.000Z&end=2012-04-05"
"2012-04-05T00:00:15.000Z&end=2012-04-26"
"2012-04-26T00:00:15.000Z&end=2012-05-17"
"2012-05-17T00:00:15.000Z&end=2012-06-07"
"2012-06-07T00:00:15.000Z&end=2012-06-28"
"2012-06-28T00:00:15.000Z&end=2012-07-19"
"2012-07-19T00:00:15.000Z&end=2012-08-09"
"2012-08-09T00:00:15.000Z&end=2012-08-30"
"2012-08-30T00:00:15.000Z&end=2012-09-20"
"2012-09-20T00:00:15.000Z&end=2012-10-11"
"2012-10-11T00:00:15.000Z&end=2012-11-01"
"2012-11-01T00:00:15.000Z&end=2012-11-22"
"2012-11-22T00:00:15.000Z&end=2012-12-13"
"2012-12-13T00:00:15.000Z&end=2013-01-03"
"2013-01-03T00:00:15.000Z&end=2013-01-24"
"2013-01-24T00:00:15.000Z&end=2013-02-14"
"2013-02-14T00:00:15.000Z&end=2013-03-07"
"2013-03-07T00:00:15.000Z&end=2013-03-28"
"2013-03-28T00:00:15.000Z&end=2013-04-18"
"2013-04-18T00:00:15.000Z&end=2013-05-09"
"2013-05-09T00:00:15.000Z&end=2013-05-30"
"2013-05-30T00:00:15.000Z&end=2013-06-20"
"2013-06-20T00:00:15.000Z&end=2013-07-11"
"2013-07-11T00:00:15.000Z&end=2013-08-01"
"2013-08-01T00:00:15.000Z&end=2013-08-22"
"2013-08-22T00:00:15.000Z&end=2013-09-12"
"2013-09-12T00:00:15.000Z&end=2013-10-03"
"2013-10-03T00:00:15.000Z&end=2013-10-24"
"2013-10-24T00:00:15.000Z&end=2013-11-14"
"2013-11-14T00:00:15.000Z&end=2013-12-05"
"2013-12-05T00:00:15.000Z&end=2013-12-26"
"2013-12-26T00:00:15.000Z&end=2014-01-16"
"2014-01-16T00:00:15.000Z&end=2014-02-06"
"2014-02-06T00:00:15.000Z&end=2014-02-27"
"2014-02-27T00:00:15.000Z&end=2014-03-20"
"2014-03-20T00:00:15.000Z&end=2014-04-10"
"2014-04-10T00:00:15.000Z&end=2014-05-01"
"2014-05-01T00:00:15.000Z&end=2014-05-22"
"2014-05-22T00:00:15.000Z&end=2014-06-12"
"2014-06-12T00:00:15.000Z&end=2014-07-03"
"2014-07-03T00:00:15.000Z&end=2014-07-24"
"2014-07-24T00:00:15.000Z&end=2014-08-14"
"2014-08-14T00:00:15.000Z&end=2014-09-04"
"2014-09-04T00:00:15.000Z&end=2014-09-25"
"2014-09-25T00:00:15.000Z&end=2014-10-16"
"2014-10-16T00:00:15.000Z&end=2014-11-06"
"2014-11-06T00:00:15.000Z&end=2014-11-27"
"2014-11-27T00:00:15.000Z&end=2014-12-18"
"2014-12-18T00:00:15.000Z&end=2015-01-08"
"2015-01-08T00:00:15.000Z&end=2015-01-29"
"2015-01-29T00:00:15.000Z&end=2015-02-19"
"2015-02-19T00:00:15.000Z&end=2015-03-12"
"2015-03-12T00:00:15.000Z&end=2015-04-02"
"2015-04-02T00:00:15.000Z&end=2015-04-23"
"2015-04-23T00:00:15.000Z&end=2015-05-14"
"2015-05-14T00:00:15.000Z&end=2015-06-04"
"2015-06-04T00:00:15.000Z&end=2015-06-25"
"2015-06-25T00:00:15.000Z&end=2015-07-16"
"2015-07-16T00:00:15.000Z&end=2015-08-06"
"2015-08-06T00:00:15.000Z&end=2015-08-27"
"2015-08-27T00:00:15.000Z&end=2015-09-17"
"2015-09-17T00:00:15.000Z&end=2015-10-08"
"2015-10-08T00:00:15.000Z&end=2015-10-29"
"2015-10-29T00:00:15.000Z&end=2015-11-19"
"2015-11-19T00:00:15.000Z&end=2015-12-10"
"2015-12-10T00:00:15.000Z&end=2015-12-31"
"2015-12-31T00:00:15.000Z&end=2016-01-21"
"2016-01-21T00:00:15.000Z&end=2016-02-11"
"2016-02-11T00:00:15.000Z&end=2016-03-03"
"2016-03-03T00:00:15.000Z&end=2016-03-24"
"2016-03-24T00:00:15.000Z&end=2016-04-14"
"2016-04-14T00:00:15.000Z&end=2016-05-05"
"2016-05-05T00:00:15.000Z&end=2016-05-26"
"2016-05-26T00:00:15.000Z&end=2016-06-16"
"2016-06-16T00:00:15.000Z&end=2016-07-07"
"2016-07-07T00:00:15.000Z&end=2016-07-28"
"2016-07-28T00:00:15.000Z&end=2016-08-18"
"2016-08-18T00:00:15.000Z&end=2016-09-08"
"2016-09-08T00:00:15.000Z&end=2016-09-29"
"2016-09-29T00:00:15.000Z&end=2016-10-20"
"2016-10-20T00:00:15.000Z&end=2016-11-10"
"2016-11-10T00:00:15.000Z&end=2016-12-01"
"2016-12-01T00:00:15.000Z&end=2016-12-22"
"2016-12-22T00:00:15.000Z&end=2017-01-12"
"2017-01-12T00:00:15.000Z&end=2017-02-02"
"2017-02-02T00:00:15.000Z&end=2017-02-23"
"2017-02-23T00:00:15.000Z&end=2017-03-16"
"2017-03-16T00:00:15.000Z&end=2017-04-06"
"2017-04-06T00:00:15.000Z&end=2017-04-27"
"2017-04-27T00:00:15.000Z&end=2017-05-18"
"2017-05-18T00:00:15.000Z&end=2017-06-08"
"2017-06-08T00:00:15.000Z&end=2017-06-29"
"2017-06-29T00:00:15.000Z&end=2017-07-20"
"2017-07-20T00:00:15.000Z&end=2017-08-10"
"2017-08-10T00:00:15.000Z&end=2017-08-31"
"2017-08-31T00:00:15.000Z&end=2017-09-21"
"2017-09-21T00:00:15.000Z&end=2017-10-12"
"2017-10-12T00:00:15.000Z&end=2017-11-02"
"2017-11-02T00:00:15.000Z&end=2017-11-23"
"2017-11-23T00:00:15.000Z&end=2017-12-14"
"2017-12-14T00:00:15.000Z&end=2018-01-04"

"2021-01-22T00:00:15.000Z&end=2021-02-13"

                 
              
                
              
                          
                          # string_out = io.StringIO()
                          # print(string_out.getvalue(), file=f)
                          # print("Working on "+str(i)+": " + l0[i]) 
                      
        # except   IOError as e:
            # if z = 0:
            #     pass
            # else 
    #         #     print("Total is :" + str(z)+ " files.")                 
    # with open('D:\\infotrend\\runs\\sum-'+str2+'.txt', mode='w') as f:
    #     string_out = io.StringIO()
    #     print(string_out.getvalue(), file=f)
    #   #  print("Total is: "+ str(z))

   


########################################################  json or csv block check,    KeyError: 'data' is date range error, if that, print(dict_json['status'])

#   https://data.messari.io/api/v1/markets/binance-loom-bnb/metrics/price/time-series?beg=2021-01-22T00:00:15.000Z&end=2021-02-12&interval=15m
#  {"status":{"elapsed":6553,"timestamp":"2021-02-15T20:55:03.520256739Z","error_code":500,"error_message":"Internal Server Error"}}

##################################################################### server err

str1_list = ["2021-01-22T00:00:15.000Z&end=2021-02-12"]
for x in range(len(str1_list)):
    z=0
    els=[]
    
    for i in range(len(l0)):       
        # if i < 532:
        #     pass
        # else:
        str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
        r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
        r=r.json()   #clean_result(r)  #r = r.json()
        dict_json=json.loads(json.dumps(r))
        if dict_json.get('data')==False:
            print(dict_json.get('status'))
        else:                
            dic0 = dict_json['data']
            for k, v in dic0.items():
                if k == 'values':
                     if v != None: 
                         try:  
                              outfile = open("D:\\infotrend\\master_json\\"+ l0[i]+"-"+str2+".json", "w") 
                              json.dump(r, outfile) 
                              outfile.close()         
                               # df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                               # df.insert(0, 'mkt-pair', l0[i])
                               # df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                               # df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                              z+=1  # l2[i])
                              els.append(l0[i])
                              print("Working on "+str(i)+": " + l0[i]) 
                                 # time.sleep(0.1)
                         except json.decoder.JSONDecodeError as e:    
                              print(e)
                              time.sleep(0.3)
                              print(l0[i]+ "didn't go through") 
                              continue #Total is :" + str(z)+ " files.")  
              with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
                  for listitem in els:
                      f.write('%s\n' % listitem)
                      f.close()
        print("Total is :"+str(z)+" files.")
################################################################################################################ count 
str1_list = ["2020-07-25T00:00:15.000Z&end=2020-08-14"]
 


 
 , "2019-05-05T00:00:15.000Z&end=2019-05-26", "2019-05-26T00:00:15.000Z&end=2019-06-16", "2019-06-16T00:00:15.000Z&end=2019-07-07", 
"2019-07-07T00:00:15.000Z&end=2019-07-28", "2019-07-28T00:00:15.000Z&end=2019-08-18", "2019-08-18T00:00:15.000Z&end=2019-09-07",
"2019-09-07T00:00:15.000Z&end=2019-09-28","2019-09-28T00:00:15.000Z&end=2019-10-18",
"2019-10-18T00:00:15.000Z&end=2019-11-07","2019-11-07T00:00:15.000Z&end=2019-11-27","2019-11-27T00:00:15.000Z&end=2019-12-18","2019-12-18T00:00:15.000Z&end=2020-01-07",
"2020-01-07T00:00:15.000Z&end=2020-01-27","2020-01-27T00:00:15.000Z&end=2020-02-16","2020-02-16T00:00:15.000Z&end=2020-03-07",
"2020-03-07T00:00:15.000Z&end=2020-03-27","2020-03-27T00:00:15.000Z&end=2020-04-16","2020-04-16T00:00:15.000Z&end=2020-05-06","2020-05-06T00:00:15.000Z&end=2020-05-26"]
"2020-09-03T00:00:15.000Z&end=2020-09-23","2020-09-23T00:00:15.000Z&end=2020-10-13",
"2020-10-13T00:00:15.000Z&end=2020-11-02","2020-11-02T00:00:15.000Z&end=2020-11-22","2020-11-22T00:00:15.000Z&end=2020-12-12","2020-12-12T00:00:15.000Z&end=2021-01-01"]
            
for x in range(len(str1_list)):
    z=0
    els=[]
    for i in range(len(l0)):       
        # if i < 532:
        #     pass
        # else:
        str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
        r = requests.get("https://data.messari.io/api/v1/markets/"+newone+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
        r=r.json()   #clean_result(r)  #r = r.json()
        dict_json=json.loads(json.dumps(r))
        if dict_json.get('data')==False:
            print(dict_json.get('status'))
        else:                
            dic0 = dict_json['data']
            for k, v in dic0.items():
                if k == 'values':
                     if v != None: 
                                                     # outfile = open("D:\\infotrend\\master_json\\"+ l0[i]+"-"+str2+".json", "w") 
                              # json.dump(r, outfile) 
                              # outfile.close()         
                               # df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                               # df.insert(0, 'mkt-pair', l0[i])
                               # df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                               # df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                              z+=1  # l2[i])
                              els.append(dic0.get("market_slug"))   #  newone)
        #                       print("Working on "+str(i)+": " + l0[i]) 
        #                          # time.sleep(0.1)
        #                  except json.decoder.JSONDecodeError as e:    
        #                       print(e)
        #                       time.sleep(0.3)
        #                       print(l0[i]+ "didn't go through") 
        #                       continue #Total is :" + str(z)+ " files.")  
        #       with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
        #           for listitem in els:
        #               f.write('%s\n' % listitem)
        #               f.close()
        # print("Total is :"+str(z)+" files.")
 
 
print(len(els))
 
 
 
 
 
  
 
 
 
 
 
 
 
 
 
 
 ############ try block not working 
for x in range(len(str1_list)):
    
    # if x <4:   # do not remove 
    
    for i in range(len(l0)):
        # if i < 1509: 
        #     pass
        # else: 
            str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
            r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
            r=r.json()   #clean_result(r)  #r = r.json()
            dict_json=json.loads(json.dumps(r)) #read().decode())
            for line in dict_json:
                j = json.loads(line)
                try:
                    if 'data' in dict_json:
                         dic0 = dict_json['data']
                         for k, v in dic0.items():
                             if k == 'values':
                                 if v != None: 
                                    df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                                    df.insert(0, 'mkt-pair', l0[i])
                                    df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                                    df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                                    z+=1  # l2[i])
                                    els.append(l0[i])
                                    print("Working on "+str(i)+": " + l0[i]) 
                    
                except json.decoder.JSONDecodeError as e:    
                            print(e)
                            time.sleep(0.3)
                            print(l0[i]+ "didn't go through") 
                            continue #Total is :" + str(z)+ " files.") 
                finally: 
                    with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
                         for listitem in els:
                              f.write('%s\n' % listitem)
                              f.write("Total is :"+str(z)+" files.")
                              f.close()
                         outfile.close()
                # else:
                    #     pa
                    
        
       
        
       
              
        
       
        
       
              
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       
        
       #     pass                                                                            # only chcking l1 list to save time, but need to change l0 4 times if needed 
        # else: 
        #     if i < 1584: 
            str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
            try: 
                r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
                r = r.json()
                dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output
                dic0 = dict_json['data']
                for k, v in dic0.items():
                    if k == 'values':
                       if v == None: 
                           pass
                       else:         
                           df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                           df.insert(0, 'mkt-pair', l0[i])
                           df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                           df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                           print("Working on "+ str(i)+" :"+ l0[i]) #+ l2[i])
                           z +=1
         else:
              pass
              except IOError as e:
    #       print(e)
                     print(e, "There is a problem.")
                 
           with open('D:\\infotrend\\runs\\sum-'+str2+'.txt', mode='w') as f:
                 string_out = io.StringIO()
                 print(string_out.getvalue(), file=f)
                 print("Total is: "+ str(z))

####################################################################################









str1_list = ["2013-05-09T00:00:15.000Z&end=2013-05-30", "2013-05-30T00:00:15.000Z&end=2013-06-20",
"2013-06-20T00:00:15.000Z&end=2013-07-11",
"2013-07-11T00:00:15.000Z&end=2013-08-01",
"2013-08-01T00:00:15.000Z&end=2013-08-22",
"2013-08-22T00:00:15.000Z&end=2013-09-12",
"2013-09-12T00:00:15.000Z&end=2013-10-03",
"2013-10-03T00:00:15.000Z&end=2013-10-24",
"2013-10-24T00:00:15.000Z&end=2013-11-14",
"2013-11-14T00:00:15.000Z&end=2013-12-05",
"2013-12-05T00:00:15.000Z&end=2013-12-26",
"2013-12-26T00:00:15.000Z&end=2014-01-16",
"2014-01-16T00:00:15.000Z&end=2014-02-06",
"2014-02-06T00:00:15.000Z&end=2014-02-27",
"2014-02-27T00:00:15.000Z&end=2014-03-20",
"2014-03-20T00:00:15.000Z&end=2014-04-10",
"2014-04-10T00:00:15.000Z&end=2014-05-01",
"2014-05-01T00:00:15.000Z&end=2014-05-22",
"2014-05-22T00:00:15.000Z&end=2014-06-12",
"2014-06-12T00:00:15.000Z&end=2014-07-03",
"2014-07-03T00:00:15.000Z&end=2014-07-24",
"2014-07-24T00:00:15.000Z&end=2014-08-14",
"2014-08-14T00:00:15.000Z&end=2014-09-04",
"2014-09-04T00:00:15.000Z&end=2014-09-25",
"2014-09-25T00:00:15.000Z&end=2014-10-16",
"2014-10-16T00:00:15.000Z&end=2014-11-06",
"2014-11-06T00:00:15.000Z&end=2014-11-27",
"2014-11-27T00:00:15.000Z&end=2014-12-18",
"2014-12-18T00:00:15.000Z&end=2015-01-08",
"2015-01-08T00:00:15.000Z&end=2015-01-29",
"2015-01-29T00:00:15.000Z&end=2015-02-19",
"2015-02-19T00:00:15.000Z&end=2015-03-12",
"2015-03-12T00:00:15.000Z&end=2015-04-02",
"2015-04-02T00:00:15.000Z&end=2015-04-23",
"2015-04-23T00:00:15.000Z&end=2015-05-14",
"2015-05-14T00:00:15.000Z&end=2015-06-04",
"2015-06-04T00:00:15.000Z&end=2015-06-25",
"2015-06-25T00:00:15.000Z&end=2015-07-16",
"2015-07-16T00:00:15.000Z&end=2015-08-06",
"2015-08-06T00:00:15.000Z&end=2015-08-27",
"2015-08-27T00:00:15.000Z&end=2015-09-17",
"2015-09-17T00:00:15.000Z&end=2015-10-08",
"2015-10-08T00:00:15.000Z&end=2015-10-29",
"2015-10-29T00:00:15.000Z&end=2015-11-19",
"2015-11-19T00:00:15.000Z&end=2015-12-10",
"2015-12-10T00:00:15.000Z&end=2015-12-31",
"2015-12-31T00:00:15.000Z&end=2016-01-21",
"2016-01-21T00:00:15.000Z&end=2016-02-11",
"2016-02-11T00:00:15.000Z&end=2016-03-03",
"2016-03-03T00:00:15.000Z&end=2016-03-24",
"2016-03-24T00:00:15.000Z&end=2016-04-14",
"2016-04-14T00:00:15.000Z&end=2016-05-05",
"2016-05-05T00:00:15.000Z&end=2016-05-26",
"2016-05-26T00:00:15.000Z&end=2016-06-16",
"2016-06-16T00:00:15.000Z&end=2016-07-07",
"2016-07-07T00:00:15.000Z&end=2016-07-28",
"2016-07-28T00:00:15.000Z&end=2016-08-18",
"2016-08-18T00:00:15.000Z&end=2016-09-08",
"2016-09-08T00:00:15.000Z&end=2016-09-29",
"2016-09-29T00:00:15.000Z&end=2016-10-20",
"2016-10-20T00:00:15.000Z&end=2016-11-10",
"2016-11-10T00:00:15.000Z&end=2016-12-01",
"2016-12-01T00:00:15.000Z&end=2016-12-22",
"2016-12-22T00:00:15.000Z&end=2017-01-12",
"2017-01-12T00:00:15.000Z&end=2017-02-02",
"2017-02-02T00:00:15.000Z&end=2017-02-23",
"2017-02-23T00:00:15.000Z&end=2017-03-16",
"2017-03-16T00:00:15.000Z&end=2017-04-06",
"2017-04-06T00:00:15.000Z&end=2017-04-27",
"2017-04-27T00:00:15.000Z&end=2017-05-18",
"2017-05-18T00:00:15.000Z&end=2017-06-08",
"2017-06-08T00:00:15.000Z&end=2017-06-29",
"2017-06-29T00:00:15.000Z&end=2017-07-20",
"2017-07-20T00:00:15.000Z&end=2017-08-10",
"2017-08-10T00:00:15.000Z&end=2017-08-31",
"2017-08-31T00:00:15.000Z&end=2017-09-21",
"2017-09-21T00:00:15.000Z&end=2017-10-12",
"2017-10-12T00:00:15.000Z&end=2017-11-02",
"2017-11-02T00:00:15.000Z&end=2017-11-23",
"2017-11-23T00:00:15.000Z&end=2017-12-14",
"2017-12-14T00:00:15.000Z&end=2018-01-04",
"2018-01-04T00:00:15.000Z&end=2018-01-25",
"2018-01-25T00:00:15.000Z&end=2018-02-15",
"2018-02-15T00:00:15.000Z&end=2018-03-08",
"2018-03-08T00:00:15.000Z&end=2018-03-29",
"2018-03-29T00:00:15.000Z&end=2018-04-19",
"2018-04-19T00:00:15.000Z&end=2018-05-10",
"2018-05-10T00:00:15.000Z&end=2018-05-31",
"2018-05-31T00:00:15.000Z&end=2018-06-21",
"2018-06-21T00:00:15.000Z&end=2018-07-12",
"2018-07-12T00:00:15.000Z&end=2018-07-15"]
             
             
             


  
"2011-08-18T00:00:15.000Z&end=2011-09-08"
"2011-09-08T00:00:15.000Z&end=2011-09-29"
"2011-09-29T00:00:15.000Z&end=2011-10-20"
"2011-10-20T00:00:15.000Z&end=2011-11-10"
"2011-11-10T00:00:15.000Z&end=2011-12-01"
"2011-12-01T00:00:15.000Z&end=2011-12-22"
"2011-12-22T00:00:15.000Z&end=2012-01-12"
"2012-01-12T00:00:15.000Z&end=2012-02-02"
"2012-02-02T00:00:15.000Z&end=2012-02-23"
"2012-02-23T00:00:15.000Z&end=2012-03-15"
"2012-03-15T00:00:15.000Z&end=2012-04-05"
"2012-04-05T00:00:15.000Z&end=2012-04-26"
"2012-04-26T00:00:15.000Z&end=2012-05-17"
"2012-05-17T00:00:15.000Z&end=2012-06-07"
"2012-06-07T00:00:15.000Z&end=2012-06-28"
"2012-06-28T00:00:15.000Z&end=2012-07-19"
"2012-07-19T00:00:15.000Z&end=2012-08-09"
"2012-08-09T00:00:15.000Z&end=2012-08-30"
"2012-08-30T00:00:15.000Z&end=2012-09-20"
"2012-09-20T00:00:15.000Z&end=2012-10-11"
"2012-10-11T00:00:15.000Z&end=2012-11-01"
"2012-11-01T00:00:15.000Z&end=2012-11-22"
"2012-11-22T00:00:15.000Z&end=2012-12-13"
"2012-12-13T00:00:15.000Z&end=2013-01-03"
"2013-01-03T00:00:15.000Z&end=2013-01-24"
"2013-01-24T00:00:15.000Z&end=2013-02-14"
"2013-02-14T00:00:15.000Z&end=2013-03-07"
"2013-03-07T00:00:15.000Z&end=2013-03-28"
"2013-03-28T00:00:15.000Z&end=2013-04-18"
"2013-04-18T00:00:15.000Z&end=2013-05-09"
"2013-05-09T00:00:15.000Z&end=2013-05-30"
"2013-05-30T00:00:15.000Z&end=2013-06-20"
"2013-06-20T00:00:15.000Z&end=2013-07-11"
"2013-07-11T00:00:15.000Z&end=2013-08-01"
"2013-08-01T00:00:15.000Z&end=2013-08-22"
"2013-08-22T00:00:15.000Z&end=2013-09-12"
"2013-09-12T00:00:15.000Z&end=2013-10-03"
"2013-10-03T00:00:15.000Z&end=2013-10-24"
"2013-10-24T00:00:15.000Z&end=2013-11-14"
"2013-11-14T00:00:15.000Z&end=2013-12-05"
"2013-12-05T00:00:15.000Z&end=2013-12-26"
"2013-12-26T00:00:15.000Z&end=2014-01-16"
"2014-01-16T00:00:15.000Z&end=2014-02-06"
"2014-02-06T00:00:15.000Z&end=2014-02-27"
"2014-02-27T00:00:15.000Z&end=2014-03-20"
"2014-03-20T00:00:15.000Z&end=2014-04-10"
"2014-04-10T00:00:15.000Z&end=2014-05-01"
"2014-05-01T00:00:15.000Z&end=2014-05-22"
"2014-05-22T00:00:15.000Z&end=2014-06-12"
"2014-06-12T00:00:15.000Z&end=2014-07-03"
"2014-07-03T00:00:15.000Z&end=2014-07-24"
"2014-07-24T00:00:15.000Z&end=2014-08-14"
"2014-08-14T00:00:15.000Z&end=2014-09-04"
"2014-09-04T00:00:15.000Z&end=2014-09-25"
"2014-09-25T00:00:15.000Z&end=2014-10-16"
"2014-10-16T00:00:15.000Z&end=2014-11-06"
"2014-11-06T00:00:15.000Z&end=2014-11-27"
"2014-11-27T00:00:15.000Z&end=2014-12-18"
"2014-12-18T00:00:15.000Z&end=2015-01-08"
"2015-01-08T00:00:15.000Z&end=2015-01-29"
"2015-01-29T00:00:15.000Z&end=2015-02-19"
"2015-02-19T00:00:15.000Z&end=2015-03-12"
"2015-03-12T00:00:15.000Z&end=2015-04-02"
"2015-04-02T00:00:15.000Z&end=2015-04-23"
"2015-04-23T00:00:15.000Z&end=2015-05-14"
"2015-05-14T00:00:15.000Z&end=2015-06-04"
"2015-06-04T00:00:15.000Z&end=2015-06-25"
"2015-06-25T00:00:15.000Z&end=2015-07-16"
"2015-07-16T00:00:15.000Z&end=2015-08-06"
"2015-08-06T00:00:15.000Z&end=2015-08-27"
"2015-08-27T00:00:15.000Z&end=2015-09-17"
"2015-09-17T00:00:15.000Z&end=2015-10-08"
"2015-10-08T00:00:15.000Z&end=2015-10-29"
"2015-10-29T00:00:15.000Z&end=2015-11-19"
"2015-11-19T00:00:15.000Z&end=2015-12-10"
"2015-12-10T00:00:15.000Z&end=2015-12-31"
"2015-12-31T00:00:15.000Z&end=2016-01-21"
"2016-01-21T00:00:15.000Z&end=2016-02-11"
"2016-02-11T00:00:15.000Z&end=2016-03-03"
"2016-03-03T00:00:15.000Z&end=2016-03-24"
"2016-03-24T00:00:15.000Z&end=2016-04-14"
"2016-04-14T00:00:15.000Z&end=2016-05-05"
"2016-05-05T00:00:15.000Z&end=2016-05-26"
"2016-05-26T00:00:15.000Z&end=2016-06-16"
"2016-06-16T00:00:15.000Z&end=2016-07-07"
"2016-07-07T00:00:15.000Z&end=2016-07-28"
"2016-07-28T00:00:15.000Z&end=2016-08-18"
"2016-08-18T00:00:15.000Z&end=2016-09-08"
"2016-09-08T00:00:15.000Z&end=2016-09-29"
"2016-09-29T00:00:15.000Z&end=2016-10-20"
"2016-10-20T00:00:15.000Z&end=2016-11-10"
"2016-11-10T00:00:15.000Z&end=2016-12-01"
"2016-12-01T00:00:15.000Z&end=2016-12-22"
"2016-12-22T00:00:15.000Z&end=2017-01-12"
"2017-01-12T00:00:15.000Z&end=2017-02-02"
"2017-02-02T00:00:15.000Z&end=2017-02-23"
"2017-02-23T00:00:15.000Z&end=2017-03-16"
"2017-03-16T00:00:15.000Z&end=2017-04-06"
"2017-04-06T00:00:15.000Z&end=2017-04-27"
"2017-04-27T00:00:15.000Z&end=2017-05-18"
"2017-05-18T00:00:15.000Z&end=2017-06-08"
"2017-06-08T00:00:15.000Z&end=2017-06-29"
"2017-06-29T00:00:15.000Z&end=2017-07-20"
"2017-07-20T00:00:15.000Z&end=2017-08-10"
"2017-08-10T00:00:15.000Z&end=2017-08-31"
"2017-08-31T00:00:15.000Z&end=2017-09-21"
"2017-09-21T00:00:15.000Z&end=2017-10-12"
"2017-10-12T00:00:15.000Z&end=2017-11-02"
"2017-11-02T00:00:15.000Z&end=2017-11-23"
"2017-11-23T00:00:15.000Z&end=2017-12-14"
"2017-12-14T00:00:15.000Z&end=2018-01-04"
"2018-01-04T00:00:15.000Z&end=2018-01-25"
"2018-01-25T00:00:15.000Z&end=2018-02-15"
"2018-02-15T00:00:15.000Z&end=2018-03-08"
"2018-03-08T00:00:15.000Z&end=2018-03-29"
"2018-03-29T00:00:15.000Z&end=2018-04-19"
"2018-04-19T00:00:15.000Z&end=2018-05-10"
"2018-05-10T00:00:15.000Z&end=2018-05-31"
"2018-05-31T00:00:15.000Z&end=2018-06-21"
"2018-06-21T00:00:15.000Z&end=2018-07-12"
"2018-07-12T00:00:15.000Z&end=2018-07-15"
"2018-07-15T00:00:15.000Z&end=2018-08-05"
"2018-08-05T00:00:15.000Z&end=2018-08-26"
"2018-08-26T00:00:15.000Z&end=2018-09-16"
"2018-09-16T00:00:15.000Z&end=2018-10-07"
"2018-10-07T00:00:15.000Z&end=2018-10-28"
"2018-10-28T00:00:15.000Z&end=2018-11-18"
"2018-11-18T00:00:15.000Z&end=2018-12-09"
"2018-12-09T00:00:15.000Z&end=2018-12-30"
"2018-12-30T00:00:15.000Z&end=2019-01-20"
"2019-01-20T00:00:15.000Z&end=2019-02-10"
"2019-02-10T00:00:15.000Z&end=2019-03-03"
"2019-03-03T00:00:15.000Z&end=2019-03-24"
"2019-03-24T00:00:15.000Z&end=2019-04-14"
"2019-04-14T00:00:15.000Z&end=2019-05-05"
"2019-05-05T00:00:15.000Z&end=2019-05-26"
"2019-05-26T00:00:15.000Z&end=2019-06-16"
"2019-06-16T00:00:15.000Z&end=2019-07-07"
"2019-07-07T00:00:15.000Z&end=2019-07-28"
"2019-07-28T00:00:15.000Z&end=2019-08-18"
"2019-08-18T00:00:15.000Z&end=2019-09-07"
"2019-09-07T00:00:15.000Z&end=2019-09-28"
"2019-09-28T00:00:15.000Z&end=2019-10-18"
"2019-10-18T00:00:15.000Z&end=2019-11-07"
"2019-11-07T00:00:15.000Z&end=2019-11-27"
"2019-11-27T00:00:15.000Z&end=2019-12-18"
"2019-12-18T00:00:15.000Z&end=2020-01-07"
"2020-01-07T00:00:15.000Z&end=2020-01-27"
"2020-01-27T00:00:15.000Z&end=2020-02-16"
"2020-02-16T00:00:15.000Z&end=2020-03-07"
"2020-03-07T00:00:15.000Z&end=2020-03-27"
"2020-03-27T00:00:15.000Z&end=2020-04-16"
"2020-04-16T00:00:15.000Z&end=2020-05-06"
"2020-05-06T00:00:15.000Z&end=2020-05-26"
"2020-05-26T00:00:15.000Z&end=2020-06-15"
"2020-06-15T00:00:15.000Z&end=2020-07-05"
"2020-07-05T00:00:15.000Z&end=2020-07-25"
"2020-07-25T00:00:15.000Z&end=2020-08-14"
"2020-08-14T00:00:15.000Z&end=2020-09-03"
"2020-09-03T00:00:15.000Z&end=2020-09-23"

"2020-09-23T00:00:15.000Z&end=2020-10-13"
"2020-10-13T00:00:15.000Z&end=2020-11-02"
"2020-11-02T00:00:15.000Z&end=2020-11-22"
"2020-11-22T00:00:15.000Z&end=2020-12-12"
"2020-12-12T00:00:15.000Z&end=2021-01-01"
"2020-01-01T00:00:15.000Z&end=2021-01-22"
           
          
                

"2020-12-12T00:00:15.000Z&end=2021-01-01",
"2021-01-01T00:00:15.000Z&end=2021-01-22",
"2021-01-22T00:00:15.000Z&end=2021-02-12",          # mmas


####################################  nto working >>>> ???? 
str1_list = ["2020-09-0300:00:15.000Z&end=2020-09-23"]  
z=0
for x in range(len(str1_list)):      #  json or  csv block!
    for i in range(len(l0)):  
        # if i !=1584: # 1361:
        #     pass
        # else: 
            str2 = str1_list[x][0:10]+str("-")+str1_list[x][29:39]
            r = requests.get("https://data.messari.io/api/v1/markets/"+l0[i]+"/metrics/price/time-series?beg="+str1_list[x]+"T00:00:00.000Z&interval=15m", headers=headers)
            r = r.json()
            dict_json=json.loads(json.dumps(r))     # json.loads take a string as input and returns a dictionary as output
            if dict_json.get('data')==False:
                print(dict_json.get('status'))
            else: 
                dic0 = dict_json['data']
                for k, v in dic0.items():
                   if k == 'values':
                      if v != None: 
                          # outfile = open("D:\\infotrend\\2011_15min_json\\"+ l0[i]+"-"+str2+".json", "w") 
                          # json.dump(r, outfile)                  
                          
                          df = pd.DataFrame(v, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                          df.insert(0, 'mkt-pair', l0[i])
                          df['datetime'] = df['timestamp'].apply(lambda x: datetime.utcfromtimestamp(int(x)/1000).strftime('%Y-%m-%d %H:%M:%S'))  
                          df.to_csv("D:\\infotrend\\master_csv\\"+l0[i]+"-"+str2+".csv", index=False)
                          print("Working on "+ str(i)+" :"+ l0[i])
                          z+=1
                      with open('D:\\infotrend\\count\\sum-'+str2+'-'+str(z)+'.csv', 'w') as f:
                          for listitem in l0[i]:
                                  f.write('%s\n' % listitem)
                #   f.write("Total is :"+str(z)+" files.")
                                 
                          f.close()
                         

