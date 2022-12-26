"""
M이상 N이하의 소수를 구하는 문제
"""
# 소수
# 백준 1929
import math
M, N = map(int, input().split())
A = [0]*(N+1)
for i in range(2, N+1):
    A[i] = i
for i in range(2, int(math.sqrt(N))+1): # 제곱근까지만 수행
    if A[i] == 0:
        continue
    for j in range(i+i, N+1, i): # i+i부터 N+1까지 i간격으로 = 배수
        A[j] = 0
for i in range(M, N+1):
    if A[i] != 0:
        print(A[i])
"""
3 16
=3
5
7
11
13
"""