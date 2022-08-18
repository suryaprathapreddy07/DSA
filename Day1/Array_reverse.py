# write a function to reverse array or strign using recursion

def reverse(start,end,array):
    if start>end:
        return
    array[start],array[end]=array[end],array[start]
    reverse(start+1,end-1,array)

# driver code
array=[1,2,3,4,5,6,7,8,9]
start=0
end=len(array)-1
reverse(start,end,array)
print(array)
