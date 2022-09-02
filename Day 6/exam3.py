import collections
counts=collections.Counter(input2)
list1=[]
for key,value in counts.items():
    if(value>1):
        list1.append(key)
if(len(list1)==0):
    print(-1)
else:
    list1.sort()
    print(list1)
