# n으로 만들 수 있는 자연수 조합의 개수
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer +=1
    return answer

"""
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))
"""
