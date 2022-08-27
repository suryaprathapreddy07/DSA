'''A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

Input: nums = [1,2,3]
Output: [1,3,2]'''

import itertools
# bruteforce approach O(N!) worst time complexity
# def findNextPermutation(permutation):
#     possiblePermutations=list(itertools.permutations(permutation,len(permutation)))
#     possiblePermutations.sort()
#     permutationIndex=possiblePermutations.index(tuple(permutation))
#     if(permutationIndex!=len(possiblePermutations)-1):
#         nextpermutation=possiblePermutations[permutationIndex+1]
#     else:
#         nextpermutation=possiblePermutations[0]
#     return list(nextpermutation)

# optimal approach

# 1 traverse from back of the array
# 2 find index where array[i]<array[i+1]
# 3 find the index of number which is greater than number at index i using back traversing(between i to n-1)
# 4 swap the numbers at index i and j
# 5 modify the array by reversing array from index i+1 to n to get next permutation

def findNextPermutation(nums):
    n = len(nums)
    i = n-2
    while (i >= 0 and nums[i] >= nums[i+1]):          # step2
        i = i - 1
    if i >= 0:
        j = n-1
        while (j >= 0 and nums[j] <= nums[i]):
            j = j-1
        nums[i], nums[j] = nums[j], nums[i]     # swap
    nums[i+1:] = list(reversed(nums[i+1:]))     # step3
    print(nums)






# driver code
permutation = [1, 3, 5,2]
findNextPermutation(permutation)
