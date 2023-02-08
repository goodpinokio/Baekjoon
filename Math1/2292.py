a = int(input())

start_num = 1
cnt = 1
while a > start_num :
    start_num += 6 * cnt
    cnt += 1
    
print(cnt)