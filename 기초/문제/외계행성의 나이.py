def solution(age):
    e = list(enumerate(list("abcdefghij")))
    return "".join(e[int(i)][1] for i in list(str(age)))

print(solution(23)) #cd
print(solution(51)) #fb
print(solution(100)) #baa

"""
# char형 문자번호 a가 97번으로 시작한다는 점을 착안
def solution(age):
    return ''.join([chr(int(i)+97) for i in str(age)])
"""