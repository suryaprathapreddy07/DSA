'''Write an efficient program to print all the duplicates and their counts in the input string'''

from collections import defaultdict


string = "test string"
def duplicates(string):
    count=defaultdict(int)
    for i in string:
        count[i]+=1
    return count

for i,value in duplicates(string).items():
    if(value>1):
        print(i,f'count={value}')
