"""
최소 비용 신장 트리(MST)라고 한다.

모든 노드가 연결된 트리(Spanning Tree)에서
최소의 비용으로 모든 노드가 연결된 트리를 말한다.

방법
Kruskal : 전체 간선 중 작은 것부터 연결 (유니온 파인드 선행)
Prim : 현재 연결된 트리에 이어진 간선 중 가장 작은 것을 추가

Edge 저장 리스트(int, int)[]
 - 무게 최대: 1e6 > int가능
 - 정점 번호 최대: 1e4 > int가능
정점 방문 : bool[]
MST 비용 : int(최대 2^31보다 이내)


1. 아이디어
- MST 기본문제 (암기)
- 간선을 인접리스트에 넣기
- 힙에 시작점 넣기
- 힙이 빌 때까지 다음 작업을 반복
(힙 최소값 꺼내기, 노드 방문 처리, 비용 추가, 연결된 간선 힙에 넣기)

2. 시간복잡도 = MST:O(ElgE)

3. 자료구조
- 간선 저장 되는 인접리스트: (무게, 노드번호)
- 힙: (무게, 노드번호)
- 방문 여부 : bool[]
- MST 결과값 : int

"""

import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
edge = [[] for _ in range(V+1)] # 인덱스 하나 늘려서 바로 사용할 수 있게
chk = [False] * (V+1)
rs = 0
for i in range(E):
    a,b,c = map(int, input().split())
    edge[a].append([c,b]) # 노드 이어주기
    edge[b].append([c,a]) # 노드 이어주기

heap = [[0,1]] # 시작점 v가 1이므로 시작점은 1이 된다.

while heap:
    w, each_node = heapq.heappop(heap) # 무게, 각 노드 = 힙큐에서 힙을 꺼냄
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w # 결과 무게 에지를 합산
        for next_edge in edge[each_node]: # each_node에 붙은 다음번 간선
            if chk[next_edge[1]] == False: # 두번째 노드를 방문하지 않았다면(다음 노드를 방문하지 않았다면)
                heapq.heappush(heap, next_edge) # 힙에다가 다음 값을 넣어줌
print(rs)

"""
3 3
1 2 1
2 3 2
1 3 3
= 3
"""