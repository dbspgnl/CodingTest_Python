# 다익스트라
import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
v,e = map(int, input().split())
k = int(input())
edge = [[] for _ in range(v+1)]
dist = [INF] * (v+1)
for i in range(e):
    a,b,w = map(int, input().split())
    edge[a].append([w,b])
dist[k] = 0
heap = [[0,k]]
while heap:
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew: continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
            heapq.heappush(heap, [dist[nv], nv])
for i in range(1, v+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])