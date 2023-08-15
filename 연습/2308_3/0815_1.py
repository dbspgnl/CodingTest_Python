
import heapq
def solution(n, works):
    if n >= sum(works): return 0 # 작업 >= 야근 = 야근이 없다.
    works = [-w for w in works] # 마이너스 처리
    heapq.heapify(works)
    for _ in range(n):
        i = heapq.heappop(works) # 가장 큰 값
        i += 1 # 부호 반대로 처리
        heapq.heappush(works, i)
    return sum([x ** 2 for x in works])

print(solution(4, [4, 3, 3])) # 12
print(solution(1, [2, 1, 2])) # 6
print(solution(3, [1,1])) # 0