def solution(strlist):
    answer = []
    for word in strlist:
        answer.append(len(word))
    return answer

print(solution(["We", "are", "the", "world!"])) # [2, 3, 3, 6]

"""
def solution(strlist):
    return list(map(len, strlist))
"""