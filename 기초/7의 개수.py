def solution(array):
    return sum(1 for i in "".join(str(array)) if i == "7")

print(solution([7,77,17])) # 4

"""
def solution(array):
    return str(array).count('7')
"""