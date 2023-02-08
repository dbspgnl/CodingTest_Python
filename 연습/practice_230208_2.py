"""
최소 스패닝 트리
# 노드 수 / 엣지 수 / 인접리스트 = 모두 이었을 때 최단 거리 (시작 노드:1)
4 4
1 2 3
2 3 4
1 4 5
4 2 3
= 10
"""

import sys
import heapq
input = sys.stdin.readline
n,e = map(int, input().split())
eList = [[]for _ in range(n+1)]
chk = [False]*(n+1)
rs = 0
for i in range(e): # 양방향 인접리스트
    a,b,w = map(int, input().split())
    eList[a].append([w,b])
    eList[b].append([w,a])
heap = [[0,1]]
while heap:
    ew, en = heapq.heappop(heap)
    if chk[en] == False:
        chk[en] = True
        rs += ew
        for nList in eList[en]:
            if chk[nList[1]] == False:
                heapq.heappush(heap, nList)
print(rs)

