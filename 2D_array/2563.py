import sys

ary = [[0 for _ in range(101)]for _ in range(101)]
a = int(input())
for _ in range(a):
    x,y = map(int,input().split())
    
    for row in range(x,x+10):
        for col in range(y,y+10):
            ary[row][col] = 1
result = 0

for i in ary:
    result += i.count(1)
print(result)
    
