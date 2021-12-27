fileFull = open("Code/Data/Name & Value.txt",'r')
fileValue = open("Code\Data\Value (Without Enter).txt",'r')

for i in fileValue: 
    values = i.split(';')
    for value in values:
        value = value.split(',')
        lower = value[:3]
        upper = value[3:]
        print(f'{lower} ------- {upper}')
        
