rooms=[5,3,7,14,18,1,18,4,8,3]
k=15
n=10
st=0
end=0
curSum=0
resList=[]
for i in range(len(rooms)):
    curSum+=rooms[i]
    print(curSum)
    end=i
    if(curSum>k):
        curSum=0
        st=i+1
    if(curSum==k):
        resList.append([st+1,end+1])
        st=i
        curSum=0
resList.sort()
print(' '.join(resList[0]))
