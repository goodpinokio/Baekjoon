def sosu(x):
    if x==1:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

while True:
    n = int(input())
    count = 0
    if n==0:
        break
    for i in range(n,2*n+1):
        if sosu(i):
            count += 1
    print(count)