# 주어진 n에 근접한 자연수 i!를 구하라. 팩토리 임을 주의.
# n 최대 3,628,800임으로 범위는 최대 12까지임.
import math
def solution(n):
    for i in range(1,12):
        if n < math.factorial(i):
            return i-1

print(solution(3628800)) # 10
print(solution(7)) # 3
