# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# solve using Kadane's algorithm

from tracemalloc import start


def maxSumSubArray(array):
    curSum=0
    maxSum=0
    startIndex,endIndex,PosOfIndex=0,0,0;
    for i in range(len(array)):
        curSum+=array[i]
        if(curSum>maxSum):
            maxSum=curSum
            startIndex=PosOfIndex
            endIndex=i
        if(curSum<0):
            curSum=0
            PosOfIndex=i+1
    return (maxSum,array[startIndex:endIndex+1])

# driver code
array=[-2,1,-3,4,-1,2,1,-5,4]
maxSum,subArray=maxSumSubArray(array)
print(maxSum,subArray)


