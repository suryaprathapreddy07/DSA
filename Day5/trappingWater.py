'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

def trap(height):
    left = []
    right = []
#         code for creating left array
    bigleftBlock = 0
    for i in height:
        bigleftBlock = max(bigleftBlock, int(i))
        left.append(bigleftBlock)
    print(left)
#       code for creating right array:
    bigrightBlock = 0
    for i in height[::-1]:
        bigrightBlock = max(bigrightBlock, i)
        right.append(bigrightBlock)
    rightreverse = right[::-1]
    print(rightreverse)
#       code for calculating units of water
    water = 0
    for i in range(len(height)-1):
        water += min(left[i], rightreverse[i])-height[i]
    return water


# driver code
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
