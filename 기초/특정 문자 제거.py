def solution(my_string, letter):
    return my_string.replace(letter, "")

print(solution("abcdef", "f")) # "abcde"
print(solution("BCBdbe", "B")) # "Cdbe"

# -----
def solution2(my_string):
    for word in ["a", "e", "i", "o", "u"]:
        my_string = my_string.replace(word, "")
    return my_string

print(solution2("nice to meet you")) #"nc t mt y"

def solution2_1(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
# my_string에서 하나씩 가져온 i인데 만약 aeiou에 포함되어 있지 않다면
# 그것들로만 join해서 묶어줌 = 포함되지 않은 글자들은 빼줌

import re
def solution2_2(my_string):
    return re.sub('[aeiou]', '', my_string)

# -----
