count = int(input())
num = list(map(int,input().split()))
max_num = max(num)

new_list = []

for i in num:
    new_list.append(i/max_num*100)
test_avg = sum(new_list)/count
print(test_avg)
