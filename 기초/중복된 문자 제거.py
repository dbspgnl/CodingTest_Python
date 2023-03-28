def solution(my_string):
    result = []
    for w in list(my_string): # 문자열은 그냥 해도 된다...
        if w not in result:
            result.append(w)
    return "".join(result)

print(solution("people")) #"peol"
print(solution("We are the world")) #"We arthwold"

"""
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
    
    seq = ('name', 'age', 'sex')

dict_1 = dict.fromkeys(seq)
print(dict_1)

dict_2 = dict.fromkeys(seq, 10)
print(dict_2)

## result ##
{'age':None, 'name':None, 'sex':None}
{'age':10, 'name':10, 'sex':10}
"""