def solution(my_string):
    answer = []
    for w in my_string:
        if w.isnumeric():
            answer.append(w)
    return sorted(map(int, answer))

print(solution("hi12392")) # [1, 2, 2, 3, 9]
print(solution("p2o4i8gj2")) # [2, 2, 4, 8]
