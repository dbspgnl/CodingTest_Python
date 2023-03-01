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
import sys
input = sys.stdin.readline
import heapq
inf = sys.maxsize
v,e = map(int, input().split())
k = int(input())
eList = [[] for _ in range(v+1)]
dist = [inf] * (v+1)

for _ in range(e):
    a,b,w = map(int, input().split())
    eList[a].append([w,b])

heap = [[0,k]]
dist[k] = 0
while heap:
    ew, ev = heapq.heappop(heap) # ew: 현재비용(최단거리) ev: 노드
    if dist[ev] != ew: continue # 현재 가중치가 최소가 아니면 의미없음으로
    for nw, nv in eList[ev]: # 해당 노드의 최소 거리가 값이
        if dist[nv] > ew + nw: # 현재 간선과 다음 간선의 합보다 크면
            dist[nv] = ew + nw # 갱신
            heapq.heappush(heap, [dist[nv], nv])
for i in range(1, v+1):
    if dist[i] == inf: print("INF")
    else: print(dist[i])