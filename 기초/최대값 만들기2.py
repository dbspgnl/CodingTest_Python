def solution(numbers):
    numbers.sort()
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])

print(solution([1, 2, -3, 4, -5])) # 15
print(solution([0, -31, 24, 10, 1, 9])) # 240