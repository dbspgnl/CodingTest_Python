def solution(my_string):
    answer = ''
    for w in my_string:
        if w.islower():
            answer += w.upper()
        else:
            answer += w.lower()
    return answer

print(solution("cccCCC")) # CCCccc
print(solution("abCdEfghIJ")) # ABcDeFGHij

"""
def solution(my_string):
    return my_string.swapcase()
    
def solution(my_string):
    return ''.join([x.lower() if x.isupper() else x.upper() for x in my_string])
"""