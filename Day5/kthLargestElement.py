'''Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4'''

# bruteforce solution as well as optimal solution
def largestNumber(array,k):
    array.sort()
    print(array[-k])


# driver code
array1=[3,2,3,1,2,4,5,5,6]
array2=[3,2,1,5,6,4]
largestNumber(array1,4)
largestNumber(array2,2)