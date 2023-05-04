def solution(n):
    return 1 if int(n**(1/2)) == n**(1/2) else 2
    # return 1 if (n ** 0.5).is_integer() else 2

print(solution(144))
print(solution(976))