def solution(my_string):
    return eval(my_string)

print(solution("3 + 4"))

"""
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
# sum을 하기 위해 +로 전부 쪼갠다. 빼기는 음수로 처리한다. 
"""