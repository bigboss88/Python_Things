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
    ntable=[]
    num_table =[]
    for field in fields:
        num_table.append(hmap[field])
        print(num_table)
    for row in table:
        cool_table =[]
        for i in num_table:
           # print(i)
            cool_table.append(row[i])
            #print(cool_table)
        ntable.append(cool_table)
    return ntable

def row2dict(hmap, row):
    dict = {}
    i=0
    for key in hmap:
        dict[key] = row[hmap[key]]
        i+=1
    return dict


if __name__ == "__main__":
    table = read_csv('test1.csv')
    #hmap = header_map(table[0])    
    #print(row2dict(hmap,table[1]))
    print(select(table,{'name','eye colour'}))
