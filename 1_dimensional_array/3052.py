arr = []

for i in range(10):
    a = int(input())
    arr.append(a%42) #append 이용 배열의 마지막에 원소 추가
arr = set(arr) #set은 집합자료형 중복제거 필터 역할
print(len(arr))