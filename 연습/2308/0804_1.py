# 그래프
from collections import deque
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)] # 인접 리스트
    dist = [-1] * (n+1) # 거리 리스트
    for a,b, in edge:
        graph[a].append(b)
        graph[b].append(a)
    queue = deque([1])
    dist[1] = 0
    while queue:
        now = queue.popleft()
        for i in graph[now]:
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[now]+1
    for d in dist:
        if d == max(dist):
            answer +=1
    return answer
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])) #3