def solution(num, k):
    e = list(enumerate(str(num)))
    for i,v in e:
        if int(v) == k:
            return i+1
    return -1

print(solution(232443, 4)) # 4
print(solution(123456, 7)) # -1