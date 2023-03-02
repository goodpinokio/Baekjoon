n,m = map(int,input().split())
temp = [i+1 for i in range(n)]
for _ in range(m):
    i,j,k = map(int,input().split())
    temp[i-1:j] = temp[k-1:j]+temp[i-1:k-1]
print(*temp)