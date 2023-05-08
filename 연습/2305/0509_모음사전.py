# 모음사전에서 다음 단어는 '몇번째 단어'인가?
# 이 문제는 탐색으로 분류되어 있지만 순열로 푸는 게 빠르다.
from itertools import product
def solution(word):
    answer = []
    for i in range(1,6):
        for c in product(['A','E','I','O','U'], repeat=i):
            answer.append("".join(list(c)))
    answer.sort()
    return answer.index(word)+1 # 인덱스 찾는 문제

print(solution("AAAAE")) #6
print(solution("AAAE")) #10
print(solution("I")) #1563
print(solution("EIO")) #1189