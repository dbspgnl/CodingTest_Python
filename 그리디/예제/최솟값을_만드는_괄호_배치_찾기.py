"""
백준: 1541
임의의 수열이 주어진다. 괄호를 넣어서 최소값이 나오도록 묶는 프로그램 작성.
= 최소값이므로 - 기호 앞에서 묶어주면 된다.
"""
answer = 0
A = list(map(str, input().split("-")))

def mySum(i):
    sum =0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i) # int로 변환해서 더해줌
    return sum

for i in range(len(A)):
    temp = mySum(A[i]) # 덧셈 구간의 합
    if i == 0: # 첫번째값은 바로 더함
        answer += temp
    else: # 나머지값은 빼줌 (-기호로 분리했기 때문에)
        answer -= temp

print(answer)

"""
100-40+50+74-30+29-45+43+11
=-222
"""