input1='my name is granar'
input2='a'
if(input1.count(input2)<2):
    print(-1)
else:
    array=input1.replace(' ','').split(input2)
    array2=list(map(lambda A:len(set(A)),array))
    print(max(array2))

