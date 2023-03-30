def solution(my_str, n):
    lst = [my_str[i:i+n] for i in range(0, int(len(my_str)), n)]
    return lst

print(solution("abc1Addfggg4556b",6)) # ["abc1Ad", "dfggg4", "556b"]
print(solution("abcdef123", 3)) # ["abc", "def", "123"]

"""
string = "abcdedfghijklm"
n = 4
slicing = [string[i:i+n] for i in range(0, len(string), n)]
print(slicing) # ['abcd', 'edfg', 'hijk', 'lm']
"""
