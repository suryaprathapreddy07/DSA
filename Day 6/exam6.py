# import numpy as np
import numpy
input1=3
input2=3
input3=[3,6,9,1,4,7,2,8,9]
arr=numpy.array(input3)
newArr=numpy.array_split(arr,input1)

# logic for row sum
maxRowSum=0
for i in newArr:
    rSum=sum(i)
    maxRowSum=max(rSum,maxRowSum)

# logic for max column sum
maxColSum=0
j=0
while(j<input2):
    curSum=0
    for i in range(j,len(input3),input2):
        curSum+=input3[i]
    maxColSum=max(maxColSum,curSum)
    j+=1
print(maxRowSum+maxColSum)



