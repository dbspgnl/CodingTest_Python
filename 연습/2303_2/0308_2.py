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
# 다익스트라
import sys
input = sys.stdin.readline
import heapq
inf = sys.maxsize
v,e = map(int, input().split())
k = int(input())
eList = [[] for _ in range(v+1)]
dist = [inf]*(v+1)

for _ in range(e):
    a,b,w = map(int, input().split())
    eList[a].append([w,b])

heap = [[0,k]]
dist[k] = 0
while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in eList[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])
for i in range(1, v+1):
    if dist[i] == inf: print("INF")
    else: print(dist[i])



