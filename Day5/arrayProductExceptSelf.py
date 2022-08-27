'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]'''


from array import array


def productExceptSelf(nums):
    result = []
    if (nums.count(0) == 0):
        prod = 1
        for i in nums:
            prod *= i
        for i in nums:
            result.append(prod//i)
    elif (nums.count(0) == 1):
        prod = 1
        for i in nums:
            if (i == 0):
                continue
            else:
                prod *= i
        for i in nums:
            if (i == 0):
                result.append(prod)
            else:
                result.append(0)
    else:
        for i in range(len(nums)):
            result.append(0)
    return result


# driver code
array1 = [1, 2, 3, 4]
array2 = [-1, 1, 0, -3, 3]
print(productExceptSelf(array2))
