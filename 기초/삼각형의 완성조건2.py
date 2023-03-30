def solution(sides):
    result = []
    minv = min(sides)
    midv = max(sides)
    maxv = (minv + midv)-1
    for i in range(1, midv+1):
        if i+minv > midv:
            result.append(i)
    for i in range(midv+1, maxv+1):
        result.append(i)
        result.append(i)
    return len(set(result))

print(solution([1,2])) #1
print(solution([3,6])) #5
print(solution([11,7])) #13

"""
# 삼각형 공식인듯...
def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1
"""