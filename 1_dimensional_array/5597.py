student = [i for i in range(1,31)]

for _ in range(28):
    data = int(input())
    student.remove(data)
print(min(student))
print(max(student))