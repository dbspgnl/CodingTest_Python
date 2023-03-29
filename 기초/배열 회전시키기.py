from collections import deque
def solution(numbers, direction):
    q = deque(numbers)
    if direction == "right":
        q.rotate(1)
    else:
        q.rotate(-1)
    return list(q)

print(solution([1, 2, 3], "right")) # [3, 1, 2]
print(solution([4, 455, 6, 4, -1, 45, 6], "left")) # [455, 6, 4, -1, 45, 6, 4]

"""
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
"""