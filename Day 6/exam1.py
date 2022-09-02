#
n=2
scores=[3,4]
# n=7
# scores=[1,5,3,4,5,5,4]
import collections
n=int(input())
scores=list(map(int,input().split()))
def findCount(n,scores):
    count=0
    if(n<3):
        print(count)
        return
    noRepeats=set(scores)
    if(len(noRepeats)==n):
        print(n-2)
        return
    counts=collections.Counter(scores)
    maxrepeated=max(counts)
    print(n-counts[maxrepeated])
    return

findCount(n,scores)

