'''Given a string S. For each index i(1<=i<=N-1), erase it if s[i] is equal to s[i-1] in the string.
Input:
S = aabb
Output:  ab 
Explanation: 'a' at 2nd position is
appearing 2nd time consecutively.
Similiar explanation for b at
4th position.
'''


def removeConsecutiveCharacter(s):
        array=[]
        for i in s:
            if(len(array)>0):
                if(array[-1]==i):
                    continue
            array.append(i)
        return ''.join(array)

# driver code

s='abcasssac'
print(removeConsecutiveCharacter(s))
