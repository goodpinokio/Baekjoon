num = int(input())
n=num

count =0

while True:
    first = num//10
    last = num%10
    c=(first+last) % 10
    num = (last*10)+ c
    count+=1
    if num == n:
        break
    
print(count)
    
