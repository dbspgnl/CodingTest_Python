def solution(dot):
    x, y = dot
    if x*y <0:
        return 2 if x < 0 else 4
    else:
        return 3 if x < 0 else 1
print(solution([2, 4])) # 1
print(solution([-7, 9])) # 2

"""
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
"""