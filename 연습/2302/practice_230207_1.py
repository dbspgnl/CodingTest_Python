"""
# 노드 수 / 엣지 수
# 1번노드가 2번노드에 몇 가중치로? (양방향)
3 3
1 2 1
2 3 2
1 3 3
= 3
# 모든 노드를 이른 가중치의 합은 3
"""

import sys
import heapq
input = sys.stdin.readline
v,e = map(int, input().split())
edgeList = [[] for _ in range(v+1)]
chk = [False]*(v+1)
rs = 0
for i in range(e):
    a,b,c = map(int, input().split())
    edgeList[a].append([c,b])
    edgeList[b].append([c,a])
heap = [[0,1]] # 1번 노드부터 시작
while heap:
    ew, ev = heapq.heappop(heap)
    if chk[ev] == False:
        chk[ev] = True
        rs += ew
        for nextEdgeList in edgeList[ev]:
            if chk[nextEdgeList[1]] == False: # 다음 노드가 방문되지 않으면 시행
                heapq.heappush(heap, nextEdgeList)
print(rs) # 모든 노드를 이은 가중치의 최소