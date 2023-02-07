a=int(input())
c=0

for _ in range(a):
    b = input()
    error = 0
    for i in range(len(b)-1):
        if b[i] != b[i+1]:
            d = b[i+1:]
            if d.count(b[i]) >0:
                error +=1
    if error == 0:
        c += 1
print(c)
    