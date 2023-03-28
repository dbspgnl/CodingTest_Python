def solution(my_string):
    answer = [ word.lower() for word in list(my_string)]
    return "".join(sorted(answer))

print(solution("Bcad"))

"""
def solution(my_string):
    return ''.join(sorted(my_string.lower()))
"""