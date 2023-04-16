def solution(citations):
    citations.sort(reverse=True)
    for i, v in enumerate(citations):
        if i>=v: return i
    return len(citations)

print(solution([3, 0, 6, 1, 5])) # 3

"""
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
"""