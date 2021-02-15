# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:54:18 2021

@author: WW Ent

# this writes an empty line between rows
import csv
import glob
with open('json_summary.csv', 'w') as f:
    writer = csv.writer(f)
    a = glob.glob('D:\\infotrend\\2020_15min_json\\*.json')
    writer.writerows(zip(a))       
    
"""    
import csv, os
data=[]
with open('file_sum.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    for filename in os.listdir("D:\\infotrend\\2020_15min_json\\"):
        data.append(filename)
        writer.writerow(data)
        data=[]
writeFile.close()