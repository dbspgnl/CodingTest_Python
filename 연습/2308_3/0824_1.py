# 작업할 수 있는 시간 n과 남아있는 작업 시간 배열(야근 시간) works가 주어진다.
# 남은 works은 제곱이 된다. n시간의 작업을 처리해서 최소 야근이 되도록 처리.
import heapq
def solution(n, works):
    #앞으로 작업할 수 있는 시간 n
    #추가적으로 작업해야할 작업 시간 배열 works
    if n>=sum(works): return 0 # 여유 시간이 더 많으면 야근 0
    # 마이너스 처리해서 최대값 힙으로 변경
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