# 아스키코드 응용 ord()/chr()
def solution(name):
    answer = 0
    move = len(name)-1 # 이동횟수
    dict1 = dict(zip("ABCDEFGHIJKLMN", range(14)))
    dict2 = dict(zip("AZYXWVUTSRQPO", range(13)))
    dict1.update(dict2)
    for i,c in enumerate(name):
        answer += dict1.get(c)
        next = i + 1 # A반복 체크
        while next < len(name) and name[next] == 'A':
            next += 1
        left_search = 2 * i + len(name) - next
        right_search = i + 2 * (len(name) - next)
        move = min([move, left_search, right_search])
    return answer + move

print(solution("JEROEN")) #56
print(solution("JAN")) #23
print(solution("ABAA")) #2
print(solution("BCAAABCD")) #14

"""


"""
