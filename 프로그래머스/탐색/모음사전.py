# 모음사전에서 다음 단어는 몇번째 단어인가?
from itertools import product
def solution(word):
    answer = []
    for i in range(1, 6): # product 중복 순열 반복 처리
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            answer.append("".join(list(c)))
    answer.sort()
    return answer.index(word)+1

print(solution("AAAAE")) #6
print(solution("AAAE")) #10
print(solution("I")) #1563
print(solution("EIO")) #1189

"""
# 한줄식
from itertools import product
solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1
"""