def solution(n):
    primes = list(filter(lambda v: n % v == 0, range(2, n + 1)))
    answer = []
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                answer.append(i)
                break
    return [i for i in primes if i not in answer]

print(solution(12)) # [2, 3]
print(solution(17)) # [17]
print(solution(420)) # [2, 3, 5, 7]

"""
def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer
"""