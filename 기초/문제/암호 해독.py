def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += list(cipher)[i]
    return answer

print(solution("dfjardstddetckdaccccdegk",4))
print(solution("pfqallllabwaoclk",2))

"""
def solution(cipher, code):
    return cipher[code-1::code]
"""