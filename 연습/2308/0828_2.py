import heapq
def solution(n, works):
    if n >= sum(works): return 0
    works = [-w for w in works]
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works)
        i += 1
        heapq.heappush(works, i)
    return sum([x ** 2 for x in works])

print(solution(4, [4, 3, 3])) # 12
print(solution(1, [2, 1, 2])) # 6
print(solution(3, [1,1])) # 0