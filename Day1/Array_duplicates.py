# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def containsDuplicates(array):
    if(len(array)==len(set(array))):
        return False
    return True

# Driver code
array=[1,2,3]
print(containsDuplicates(array))