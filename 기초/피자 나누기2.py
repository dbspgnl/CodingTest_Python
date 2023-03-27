def solution(n):
    for i in range(1, 100):
        if (6*i)%n == 0:
            return i

print(solution(6)) # 1
print(solution(10)) # 5
print(solution(4)) # 2

"""
import math
def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6
"""