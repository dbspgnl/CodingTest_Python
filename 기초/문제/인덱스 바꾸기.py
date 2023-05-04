def solution(my_string, num1, num2):
    answer = list(my_string)
    temp = answer[num1]
    answer[num1] = answer[num2]
    answer[num2] = temp
    return "".join(answer)

print(solution("hello",1,2)) # hlelo

"""
# 더 깔끔한 코드
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)
"""