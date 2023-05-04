def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer +=1
    return answer

print(solution([149, 180, 192, 170], 167))

"""
def solution(array, height):
    return sum(1 for a in array if a > height)
"""