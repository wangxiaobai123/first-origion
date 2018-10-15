def strtoint(chr):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[chr]


list1 = ['1','2','3','4']
list2 = map(strtoint,list1)
print(list(list2))



