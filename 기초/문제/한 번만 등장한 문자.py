from collections import Counter
def solution(s):
    result = Counter(s)
    keys = list(result.keys())
    values = list(result.values())
    array = []
    for i in range(len(values)):
        if values[i] == 1:
            array.append(keys[i])
    array = sorted(array)
    return "".join(array)

print(solution("abcabcadc")) # "d"
print(solution("abdc")) #	"abcd"
print(solution("hello")) #	"eho"

"""
# 순서가 있는 알파벳 배열을 탐색하면서 세팅한다라... 신박하다.
def solution(s):
    answer = ''
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if s.count(c) == 1:
            answer += c
    return answer

def solution(s):
    answer = "".join(sorted([ ch for ch in s if s.count(ch) == 1]))
    return answer
"""