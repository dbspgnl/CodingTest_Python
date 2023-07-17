# N(1~9)가 주어지고, 목표 number가 주어진다.
# 사직 연산만 이용해서 N을 number로 만들 때, 최솟값에 들어간 N의 횟수
# 결과가 8보다 크면 -1을 리턴
from collections import defaultdict
def solution(N, number):
    dp = defaultdict(set)
    for i in range(1,9):
        dp[i].add(int(str(N)*i)) # N, NN, NNN ...
        for j in range(1, i):
            for n1 in dp[j]:
                for n2 in dp[i - j]: # 순회하면서 4칙연산 수행
                    dp[i].add(n1 + n2)
                    dp[i].add(n1 - n2)
                    dp[i].add(n1 * n2)
                    if n2 != 0: dp[i].add(n1//n2) # 0 나누기 방지
        if number in dp[i]: return i # 찾는 값이 set에 있으면 index(n의 사용 갯수) 리턴
    return -1 # 해당하지 않으면 -1 = 최솟값이 8보다 크면

print(solution(5,12)) # 4
'''
5를 이용해 12를 구하는 방법
12 = 5 + 5 + (5 / 5) + (5 / 5) # 6번 사용
12 = 55 / 5 + 5 / 5 # 5번 사용
12 = (55 + 5) / 5 # 4번 사용
모든 경우의 수를 set에 넣어서 최소값 구하면 된다. n이 작아서 가능.
(1): 5
(2): 55
(3): 555
...
(8): 55555555
이런식으로 만들어서 사칙연산 4가지 경우를 모두 처리해서 담는다. 기하급수로 늘어난다.
5 일때 1: {5}
55 일때 2: {0, 1, 10, 55, 25}
555 일때 3: {0, 2, 4, 5, 6, 555, -20, -4, -50, 15, 11, 50, 275, 20, -5, 60, 125, 30}
5555 일때 4: {0, 1, 2, 3, 130, 5, -250, ... 12}
'''