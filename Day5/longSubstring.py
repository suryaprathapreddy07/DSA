'''Given a string s, find the length of the longest substring without repeating characters.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''

def longSubstring(string):
    left=0
    right=0
    curstr=''
    subStrings=[]
    while(left<len(string)-1):
        if(string[right] in curstr):
            subStrings.append(curstr)
            curstr=''
            left+=1
            right=left
        else:
            curstr+=string[right]
            right+=1
    
    subStrings.sort(key=lambda x:len(x))
    return len(subStrings[-1])


s = "abcabcbb"
print(longSubstring(s))

