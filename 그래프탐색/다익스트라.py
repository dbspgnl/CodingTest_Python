"""
한 노드에서 다른 모든 노드까지 가는데 최소 비용 (최소 신장 트리와 유사하다)
간선: 인접리스트, 거리배열: 초기값 무한대로 설정, 힙 시작점 추가

1. 아이디어
- 한점시작, 모든 거리 : 다익스트라
- 간선, 인접리스트 저장
- 거리배열 무한대 초기화
- 시작점 : 거리배열 0, 힙에 넣어주기
- 힙에서 빼면서 다음의 것들을 수행
    - 최신값인지 먼저 확인
    - 간선을 타고 간 비용이 더 작으면 갱신

2. 시간복잡도
- 다익스트라: O(ElgV)
    - E: 3e5
    - V : 2e4, lgV ~= 20
    - ElgV = 6e6 > 가능

3. 변수
- 힙: (비용, 노드번호)
- 거리 배열: 비용 : int[]

- 가선 저장, 인접리스트: (비용, 노드번호)[]

"""

import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split()) # 노드의 수, 간선의 수
K = int(input()) # 시작점
edge = [[] for _ in range(V+1)] # 간선 리스트는 1부터 처리하도록 V+1개 빈 값으로 만들어준다.
dist = [INF] * (V+1) # 거리 배열에 아주 큰 값을 넣는다.

for i in range(E):
    u,v,w = map(int, input().split())
    edge[u].append([w,v]) # 노드u에 무게w와 도착노드v를 넣어준다.

# 시작점 초기화
dist[K] = 0; # 거리 배열
heap = [[0,K]] # 최솟값 세팅

while heap:
    ew, ev = heapq.heappop(heap) # ew: 현재비용 ev: 노드
    if dist[ev] != ew: continue # 거리 배열에서 최신 값과 일치하는 여부 파악
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw: # 현재 간선과 다음 간선의 합보다 크면
            dist[nv] = ew + nw # 갱신
            heapq.heappush(heap, [dist[nv], nv])

for i in range(1, V+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])

"""
5 6 # 다섯개의 노드 / 여섯개의 간선
1 # 시작점 노드
5 1 1 # 5번 노드가 1번 
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
"""