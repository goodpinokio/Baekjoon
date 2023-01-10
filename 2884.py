hour,min = map(int,input().split())

if min>44:
    print(hour,min-45)
elif min<45 and hour>0:
    print(hour-1,min+15)
else:
    print(23,min+15)