"""
# 노드 수 / 엣지 수
# 1번노드가 2번노드에 몇 가중치로? (양방향)
3 3
1 2 1
2 3 2
1 3 3
= 3
# 모든 노드를 이은 가중치의 합은 3
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
eList = [[] for _ in range(n+1)]
chk = [False] * (n+1)
rs = 0

for i in range(e):
   a,b,c = map(int, input().split())
   eList[a].append([c,b])
   eList[b].append([c,a])

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

