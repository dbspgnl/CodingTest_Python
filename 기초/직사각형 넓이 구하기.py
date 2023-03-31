def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    w = max(x) - min(x)
    h = max(y) - min(y)
    area = w * h
    return area

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]])) #1
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]])) #4
print(solution([[20, 20], [40, 20], [40, 30], [20, 30]])) #4
