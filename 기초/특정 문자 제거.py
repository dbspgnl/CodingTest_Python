def solution(my_string, letter):
    return my_string.replace(letter, "")

print(solution("abcdef", "f")) # "abcde"
print(solution("BCBdbe", "B")) # "Cdbe"
