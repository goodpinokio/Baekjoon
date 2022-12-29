N = list(map(int,input().split()))

K = [1,1,2,2,2,8]

for i in range(0,len(N)):
    print(K[i] - N[i],end=' ')