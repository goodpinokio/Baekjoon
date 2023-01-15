price = int(input())
total = int(input())
sum = 0

for _ in range(total):
    bill,cnt = map(int,input().split())
    sum += bill*cnt
    
if price == sum: print('Yes')
else: print('No')

