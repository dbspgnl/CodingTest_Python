def solution(n, t):
    return n * (2 ** t)
print(solution(2,10))	#2048
print(solution(7,15))	#229,376
"""
# 2의 배수이기 때문에 이런식으로 배수 할 수 있다. 
def solution(n, t):
    return n << t
"""