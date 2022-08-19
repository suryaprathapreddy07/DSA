'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.'''



def validPalindrome(string):
    requiredString=''
    for i in string:
        if(i.isalpha()):
            requiredString+=i
    return requiredString.lower()==requiredString.lower()[::-1]

# driverCode
s = ""
print(validPalindrome(s))