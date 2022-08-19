'''There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the 
resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.'''

def searchEle(array,target,low,high):
    while(low<=high):
        mid=(low+high)//2
        if(array[mid]==target):
            return mid

        # check for first half of array
        if(array[low]<=array[mid]):
            if(array[low]<=target<array[mid]):
                high=mid-1
            else:
                low=mid+1

        # check for second half of array
        if(array[mid]<=array[high]):
            if(array[mid]<target<=array[high]):
                low=mid+1
            else:
                high=mid-1
    return 'element not found'

# driver code

rotatedArray=[4,5,6,7,0,1,2]
low=0
high=len(rotatedArray)-1
print(searchEle(rotatedArray,2,low,high))

