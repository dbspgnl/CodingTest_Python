"""
3 16 # 이 범위에 있는 소수 구하기
=3
5
7
11
13
"""
# 소수: 에라토스테네스의 체의 방식을 기본적으로 사용한다.
import math
s,e = map(int, input().split())
aList = [0] * (e+1) # 자리수가 번호가 됨

# 자리수만큼 채워주기
for i in range(2, e+1): # 1은 소수가 아님
    aList[i] = i

# 반복문으로 수행 (제곱근까지만 처리)
for i in range(2, int(math.sqrt(e))+1):
    if aList[i] == 0:
        continue # 배수면 반복
    for j in range(i+i, e+1, i): # i배수로 m+1까지 i 간격으로 모든 배수를 찾음
        aList[j] = 0 # 해당 배수의 값을 0으로 처리

# 결과를 돌면서 출력
for i in range(s, e+1):
    if aList[i] != 0:
        print(aList[i])

