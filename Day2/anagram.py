def isAnagram( s: str, t: str) -> bool:
    if(len(s)!=len(t)):
            return False
    else:
        l1=[i for i in s]
        l2=[j for j in t]
        l1.sort()
        l2.sort()
        return l1==l2

# driver code

s='surya'
t='uryat'
print(isAnagram(s,t))