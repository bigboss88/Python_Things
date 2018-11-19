import csv
from array import *
def read_csv(filename):
    out = []
    with open(filename,'rt') as csvfile:
        reader = csv.reader(csvfile,skipinitialspace=True,delimiter=',')
        for row in reader:
            out.append(row)
    return out

def header_map(table):
    obj = {}
    i=0
    for item in table:
        obj[item] = i
        i+=1
    return obj

def select(table,fields):
    hmap = header_map(table[0])
    #print(table)
    ntable=[]
    num_table =[]
    for field in fields:
        num_table.append(hmap[field])
    #print(num_table)
    for row in table:
        #print(row)
        cool_table =[]
        for i in num_table:
            #print(i)
            cool_table.append(row[i])
        ntable.append(cool_table)
    return ntable

table = read_csv('test1.csv')
print(select(table,{'name','eye colour'}))
