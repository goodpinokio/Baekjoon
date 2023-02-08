a = int(input())

line = 0
max_num = 0
while a > max_num:
    line += 1
    max_num += line
    
gap = max_num - a
if line % 2 ==0:
    top = line - gap
    under = gap + 1

else:
    top = gap + 1
    under = line - gap 
print(f'{top}/{under}')