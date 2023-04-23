def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num: # 큰 수부터 담음
            stack.pop()
            k -= 1
        stack.append(num)
    return ''.join(stack[:len(stack) - k]) #뒤에서부터 자름
print(solution("1924",2)) # 94
print(solution("1231234",3)) # 3234
print(solution("4177252841",4)) # 775841

"""
# 시간 초과
from itertools import combinations
def solution(number, k):
    lists = []
    combi = list(combinations(number, len(number)-k))
    for i in map(list, combi):
        lists.append("".join(i))
    return max(lists)
"""