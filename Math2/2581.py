m = int(input())
n = int(input())
arr = []

for i in range(m,n+1):
    if i==1:
        pass
    elif i ==2 :
        arr.append(i)
    else:
        for j in range(2,i):
            if i%j == 0:
                break
            elif j==i-1:
                arr.append(i)
if len(arr) == 0:
    print('-1')        
else:
    print(sum(arr))
    print(min(arr))