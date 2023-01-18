size = int(input())
array = list(map(int,input().split()))

maxvalue = array[0]
minvalue = array[0]
for i in array[1:]:
    if i>maxvalue:
        maxvalue = i
    elif i < minvalue:
        minvalue = i
print(minvalue, maxvalue)