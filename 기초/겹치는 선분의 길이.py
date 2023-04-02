# def solution(lines):
#     minv = 0
#     maxv = 0
#     for line in lines:
#         minv = min(minv, min(line))
#         maxv = max(maxv, max(line))
#     fix = 0-minv
#     result = [0]*(maxv-minv)
#     for s,e in lines:
#         for i in range(s+fix,e+fix):
#             result[i] += 1
#     return sum(1 for i in result if i >=2)

"""
# set을 이용한 간격을 재고, 각각의 간격이 min, max일 때 겹칠 때의 거리를 len으로 잰다.
# 응용하기는 어려워보인다.
def solution(lines):
    sets = [set(range(min(l), max(l))) for l in lines]
    return len(sets[0] & sets[1] | sets[0] & sets[2] | sets[1] & sets[2])

# 위 내용이랑 같지만 더 현실적이고 직관적인 코드
"""
def solution(lines):
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
    print(s1) # {0}
    print(s2) # {2, 3, 4}
    print(s3) # {3, 4, 5, 6, 7, 8}
    print((s1 & s2) | (s2 & s3) | (s1 & s3)) # {3, 4}
    return len((s1 & s2) | (s2 & s3) | (s1 & s3))

print(solution([[0, 1], [2, 5], [3, 9]])) #2
print(solution([[-1, 1], [1, 3], [3, 9]])) #0
print(solution([[0, 5], [3, 9], [1, 10]])) #8