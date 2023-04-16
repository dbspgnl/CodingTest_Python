def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int("".join(numbers)))

print(solution([6, 10, 2])) #6210"
print(solution([3, 30, 34, 5, 9])) #"9534330"
print(solution([0,0,0,0])) #0"