# Given an array of n integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 
# 1. Each student gets one packet.
# 2. The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

def getMinDiff(array,n):
    array.sort()
    minDiff=array[n-1]-array[0]
    for i in range(len(array)-n+1):
        subList=array[i:i+n]
        if(minDiff>(subList[-1]-subList[0])):
            minDiff=subList[-1]-subList[0]
    return minDiff


# driver code
array=[7, 3, 2, 4, 9, 12, 56]
numberOfStudents=3
print(getMinDiff(array,numberOfStudents))






