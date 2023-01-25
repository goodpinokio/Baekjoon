num = int(input())

for _ in range(num):
    score = list(map(int,input().split()))
    avg = sum(score[1:])/score[0] #평균 구함 score[0]은 학생수 
    cnt = 0
    for i in score[1:]:
        if i > avg:
            cnt += 1 #평균 이상인 학생 수
    rate = cnt/score[0] * 100
    print(f'{rate:.3f}%')