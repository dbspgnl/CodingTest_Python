"""
MST
힙 / 인접리스트 / 체크리스트
양방향 처리 / 지금 노드로 다음 노드까지 체크 후 힙에 넣음
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
    a,b,w = map(int, input().split())
    eList[a].append([w,b])
    eList[b].append([w,a])

heap = [[0,1]]
while heap:
    ew, en = heapq.heappop(heap)
    if chk[en] == False:
        chk[en] = True
        rs += ew
        for nHeap in eList[en]:
            if chk[nHeap[1]] == False:
                heapq.heappush(heap, nHeap)

print(rs)