def solution(my_string):
    print(list(my_string)) # ['j', 'a', 'r', 'o', 'n']
    print(list(reversed(list(my_string)))) # ['n', 'o', 'r', 'a', 'j']
    return ''.join(list(reversed(list(my_string))))
    # reverse()는 결과만 reversed 함수는 list로 다시 담을 수 있음
print(solution("jaron")) # "noraj"

"""
def solution(my_string):
    # return "".join(list(my_string)[::-1])
    return my_string[::-1] # 그냥 해도 됨
"""
