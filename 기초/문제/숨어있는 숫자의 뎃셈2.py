def solution(my_string):
    my_string = "".join([word if word.isnumeric() else ' ' for word in list(my_string)])
    print(my_string) # "   1 2  34   "
    number_list = list(map(int, my_string.split()))
    print(number_list) #[1, 2, 34]
    return sum(number_list) # 37

print(solution("aAb1B2cC34oOp")) # 37
print(solution("1a2b3c4d123Z")) # 133