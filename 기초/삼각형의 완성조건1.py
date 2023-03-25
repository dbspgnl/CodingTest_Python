def solution(sides):
    return 2 if max(sides) / sum(sides)  >= 0.5 else 1

print(solution([1, 2, 3])) # 2
print(solution([3, 6, 2])) # 2
print(solution([199, 72, 222])) # 1

"""
def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2
"""