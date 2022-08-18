# Write a function to return minimum and maximum in an array. Your program should make the minimum number of comparisons. 

# we can solve this using linear comparision but for good time complexity we will do this using recursion

# now we will find min and max in first and second half of array using recursion
def minMax(low,high,array):
    minEle=array[low]
    maxEle=array[low]

    # case1 :if one element present in array
    if(low==high):
        minEle=array[low]
        maxEle=array[low]
        return (minEle,maxEle)
    # case2 :if only two elements are present in array
    elif(high==low+1):
        if(array[low]<array[high]):
            minEle=array[low]
            maxEle=array[high]
        if(array[low]>array[high]):
            minEle=array[high]
            maxEle=array[low]
        return (minEle,maxEle)
    # case 2: if more than two elements are present
    else:
        mid=int((low+high)/2)
        minEle1,maxEle1=minMax(low,mid,array)
        minEle2,maxEle2=minMax(mid+1,high,array)
    return (min(minEle1,minEle2),max(maxEle1,maxEle2))

# driver code
array=[10,20,45,2,5,4,84,56,1,2,45,45,8,4,75,56]
low=0
high=len(array)-1
print(minMax(low,high,array))

