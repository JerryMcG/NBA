import csv
import os

#assign variable for data load and the path
data = os.path.join('Resources', '2018-19_pbp.csv')

#open NBA data
with open(data) as NBA_2018_2019:
    #read the file
    NBA_read = csv.reader(NBA_2018_2019)
    #print the header row 
    headers = next(NBA_read)
    print(headers)
#analysis of the data