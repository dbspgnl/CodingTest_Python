"""
여러개의 값이 주어지고 특정 범위까지의 합을 구하는 문제
S[i] = S[i-1]+A[i] 공식을 이용한다.
"""
# 구간 합
# 백준 11659
# 숫자 갯수, 질의 갯수
# 숫자 배열
# 합 배열
# 변수
import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0
for i in numbers:
    temp = temp + i
    prefix_sum.append(temp) # 합 배열 만들기
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e]-prefix_sum[s-1])
"""
5 3
5 4 3 2 1
1 3
2 4
5 5
= 12
9
1
"""