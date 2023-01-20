a,b = map(int,input().split())
array = list(map(int,input().split()))

for i in range(a):
    if array[i] < b:
        print(array[i], end=" ")