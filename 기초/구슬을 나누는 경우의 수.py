import math
def solution(balls, share):
    return int(math.factorial(balls) / (math.factorial((balls-share)) * math.factorial(share)))

print(solution(5,3)) #10

"""
# 조합은 함수가 따로 있다. 
import math
def solution(balls, share):
    return math.comb(balls, share)
"""