#def solution(n):
#    return n-(sum([1 for i in range(4, n+1) if i % 2 != 0 and i % 3 != 0 and i % i == 0 and int(i**(1/2)) != i**(1/2)])+3)
# 49는 합성수이지만 2와 3으로 나눠 떨어지지 않는다... 특수 케이스가 존재한다.
# 따라서 소수가 아닌 애들을 모두 걸러내야한다.
def solution(n):
    answer = 0
    for i in range(4, n + 1): # 4부터 시작
        for j in range(2, int(i ** 0.5) + 1): # 제곱근 있는 모든 값으로 시도
            if i % j == 0: # 2,3은 보통 들어가고 제곱근으로도 시도함
                answer += 1
                break
    return answer

print(solution(10)) #5
print(solution(15)) #8
print(solution(49)) #8

"""
def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))
"""
