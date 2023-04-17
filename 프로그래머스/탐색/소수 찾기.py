from itertools import permutations

def solution(numbers):
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers) + 1): # 모든 경우 순열로
        per += list(permutations(nums, i)) # [('1',), ('7',), ('1', '7'), ('7', '1')]
    new_nums = [int(("").join(p)) for p in per] # [71, 17, 1, 7]
    new_nums = set(new_nums)
    answer = []
    for n in new_nums:
        if n < 2:  # 0,1은 소수 아님
            continue
        check = True
        for i in range(2, int(n ** 0.5) + 1):  # n의 제곱근까지만
            if n % i == 0:  # 나눠 떨어지면 소수아님
                check = False
                break
        if check:
            answer.append(n)
    return len(answer)

print(solution("17")) #3
print(solution("011")) #2
print(solution("1111111")) #1

"""
from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)
"""