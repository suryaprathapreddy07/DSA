input1=5
input2=[1,2,-3,4,-5]
maxSum=0
curSum=0
for i in input2:
    curSum+=i
    if(curSum>maxSum):
        maxSum=curSum
    if(curSum<0):
        curSum=0
print(maxSum)