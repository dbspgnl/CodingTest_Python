def solution(numbers):
    return list(map(lambda x : x*2, numbers))

print(solution([1, 2, 100, -99, 1, 2, 3]))
# [2, 4, 200, -198, 2, 4, 6]

"""
def solution(numbers):
    return [num*2 for num in numbers]
"""