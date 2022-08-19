def validParenthesis(string):
    open=['(','{','[']
    close=[')','}',']']
    stack=[]
    for i in range(len(string)):
        if(string[i] in open):
            stack.append(string[i])
        elif(string[i] in close):
            index=close.index(string[i])
            if(len(stack)>0):
                if(stack[-1]==open[index]):
                    stack.pop()
            else:
                return False
        else:
            return False
    return len(stack)==0






# driver code
s1 = "()[]{}"
s2 = "(]"
s3='{[()]}'
s4="(])"
s5=']'
print(validParenthesis(s5))