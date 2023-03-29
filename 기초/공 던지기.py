def solution(numbers, k):
    return numbers[((k-1) * 2)%len(numbers)]

print(solution([1, 2, 3, 4], 2)) # 3
print(solution([1, 2, 3, 4, 5, 6], 5)) # 3
print(solution([1, 2, 3], 3)) # 3