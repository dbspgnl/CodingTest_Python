"""
# 노드 수 / 간선 수
# 시작 노드
# 인접 리스트
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
= 0
2
3
7
INF
# 시작점에서 각 노드까지의 거리
"""
# 다익스트라는 특정 지점에서 모든 지점까지의 거리를 구한다 (최소 inf)
import sys
import heapq
inf = sys.maxsize
input = sys.stdin.readline
n,e = map(int, input().split())
k = int(input())
eList = [[] for _ in range(n+1)]
dist = [inf]*(n+1)

for _ in range(e):
    a,b,w = map(int, input().split())
    eList[a].append([w,b])

dist[k] = 0
heap = [[0,k]]
while heap:
    ew, en = heapq.heappop(heap)
    if ew != dist[en]: continue
    for nw, nn in eList[en]:
        if dist[nn] > ew + nw:
            dist[nn] = ew + nw
            heapq.heappush(heap, [dist[nn], nn])

for i in range(1, n+1):
    if dist[i] == inf: print("INF")
    else: print(dist[i])