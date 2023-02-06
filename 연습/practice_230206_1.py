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

# 노드 수 / 간선 수
# 시작 노드
# 인접리스트

import sys
import heapq
input  = sys.stdin.readline
inf = sys.maxsize
v,e = map(int, input().split())
k = int(input()) # 시작노드
edgeList = [[] for _ in range(v+1)] # 노드 번호 만큼 인접리스트
dist = [inf] * (v+1)
for i in range(e):
    a,b,w = map(int, input().split())
    edgeList[a].append([w,b])
dist[k] = 0
heap = [[0,k]]
while heap:
    ew, ev = heapq.heappop(heap) # 힙에서 가져오기
    if dist[ev] != ew: continue # 만약에 힙에서 꺼내 노드의 최소거리가 현재 값과 다르면 의미없음
    for nw, nv in edgeList[ev]:
        if dist[nv] > ew + nw: # 저정된 최소거리가 지금 이동거리보다 크면
            dist[nv] = ew + nw # 더 작은 값으로 갱신
            heapq.heappush(heap, [dist[nv], nv]) # 갱신된 노드 정보로 다시 찾기
for i in range(1, v+1):
    if dist[i] == inf: print("INF")
    else: print(dist[i])
