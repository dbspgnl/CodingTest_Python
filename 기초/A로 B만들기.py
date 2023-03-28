def solution(before, after):
    for i in before:
        after = after.replace(i, "", 1)
    return 1 if after == "" else 0

print(solution("olleh", "hello")) # 1
print(solution("allpe", "apple")) # 0
