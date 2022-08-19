# recursive approach

def searchEle(array, low, high, n):
    if (low <= high):
        mid = int((low+high)/2)
        if (array[mid] == n):
            return mid
        elif (array[mid] < n):
            return searchEle(array, mid+1, high, n)
        else:
            return searchEle(array, low, mid-1, n)
    else:
        return 'element not found'


array = [15, 15, 4, 22, 5, 7, 1, 8, 8, 1, 25, 8, 1, 5, 55, 112]
array.sort()
print(array)
low = 0
high = len(array)-1
print(searchEle(array, low, high, 25))
