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
        #print(num_table)
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

def check_row(row,op):
    left = op[0]
    operation = op[1]
    right = op[2]
    if(operation == 'OR'):
        return check_row(row,left) or check_row(row,right)
    elif(operation == 'AND'):
        return check_row(row,left) and check_row(row,right)
    #print(left)
    #print(operation)
    #print(right)
    value = row[left]
    if(type(right) is int):
        try:
            value = int(value)
        except ValueError:
            return False
    if(operation == '=='):
        if(value == right):
            return True
        return False
    elif(operation == '<='):
        if(value <= right):
            return True
        return False
    elif(operation == '>='):
        if(value >= right):
            return True
        return False
if __name__ == "__main__":
    table = read_csv('test1.csv')
    #hmap = header_map(table[0])    
    #print(row2dict(hmap,table[1]))
    print(select(table,{'name','eye colour'}))
    row = {'name': 'Bob', 'age': '5', 'eye colour': 'blue'}
    print(check_row(row, ('age', '==', 5)))
    print(type(('age', '==', 5)))