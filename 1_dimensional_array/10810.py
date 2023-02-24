n,m = map(int,input().split())

base = [0] * (n+1)

for _ in range(m):
    i,j,k = map(int,input().split())
    for e in range(i,j+1):
        base[e] = k
for i in range(1,n+1):
    print(base[i], end=' ')