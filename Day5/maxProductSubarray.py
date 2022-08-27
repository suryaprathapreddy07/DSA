'''Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.'''




def maxProduct(array):
    maximum=array[0]
    minimum=array[0]
    result=array[0]
    for i in range(1,len(array)-1):
        if(array[i]<0):
            maximum,minimum=minimum,maximum
        
        maximum=max(array[i],maximum*array[i])
        minimum=min(array[i],minimum*array[i])
        result=max(result,maximum)
    return result

# driver code
array1=[2,3,-2,4]
array2=[-2,0,-1]
print(maxProduct(array2))