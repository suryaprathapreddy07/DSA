'''You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4'''

# bruteforce approach
# def findNumbers(array):
#     array.sort()
#     repeated=0
#     missing=0
#     for i in range(len(array)-1):
#         if(array[i]==array[i+1]):
#             repeated=array[i+1]
#             missing=array[i]+1
#             break
#     print([repeated,missing])

# optimal approach
def findNumbers(array):
    n=len(array)
    sum1=sum(array)
    sumToN=n*(n+1)//2
    arrayWithoutRepeated=list(set(array))
    sum2=sum(arrayWithoutRepeated)
    repeated=sum1-sum2
    missing=sumToN-sum2
    print(repeated,missing)




# driver code
array1=[3,1,2,5,3]
array2=[2,2]
findNumbers(array1)
