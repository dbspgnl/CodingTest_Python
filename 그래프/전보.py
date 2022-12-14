"""
최단거리 구하는 문제
도시 n과 거리m 시작도시를 첫번째 줄에서 입력받는다.
방향성 있는 거리를 시작도시 도착도시 거리시간 순으로 입력받을 때,
시작 도시로부터 최대한 많은 도시로 전보할 경우,
전보하는 도시의 수와 가장 오래 걸리는 시간은?
"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
n, m, start = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m): # 간선 정보
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
dijkstra(start)
count=0 # 도시 수 카운팅
max_distance=0 # 가장 먼 거리
for d in distance:
    if d != 1e9: # 갈 수 있는 도시
        count += 1
        max_distance = max(max_distance, d)
print(count-1, max_distance)
"""
3 2 1
1 2 4
1 3 2
= 2 4
"""