'''Convert a sentence into its equivalent mobile numeric keypad sequence
Input : GEEKSFORGEEKS
Output : 4333355777733366677743333557777
For obtaining a number, we need to press a
number corresponding to that character for 
number of times equal to position of the 
character. For example, for character C, 
we press number 2 three times and accordingly.'''

strs=['2','22','222','3','33','333','4','44','444','5','55','555','6','66','666','7','77','777','7777','8','88','888','9','99','999','9999']

def convertString(str):
    resultStr=''
    for char in str:
        if(char==' '):
            resultStr+='0'
        else:
            index=abs(65-ord(char))
            print(index)
            resultStr+=strs[index]
    return resultStr

# driver code
str1='GEEKSFORGEEKS'
print(convertString(str1))