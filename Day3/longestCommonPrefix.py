'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".'''





def longestCommonPrefix(strs):
    if(len(strs)==1):
        return strs[0]
    if(len(strs[0])==0):
        return ""
    strs.sort(key=lambda x:len(x))
    curStr=''
    result=''
    for i in strs[-1]:
        curStr+=i
        for i in strs:
            if(curStr not in i):
                return result
        result=curStr



# driver code
strs1 = ["flower","flow","flight"]
strs2= ["dog","racecar","car"]
strs3=["ab", "a"]
strs4=[""]
strs5=["",""]
strs6=['a']

print(longestCommonPrefix(strs6))