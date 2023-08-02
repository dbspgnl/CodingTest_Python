# 최소신상트리
import sys
import heapq
input = sys.stdin.readline
v,e = map(int, input().split())
edge = [[] for _ in range(v+1)]
chks = [False]*(v+1)
rs = 0
for i in range(e):
    a,b,w = map(int, input().split())
    edge[a].append([w,b])
    edge[b].append([w,a])
heap = [[0,1]]
while heap:
    ew, en = heapq.heappop(heap)
    if chks[en] == False:
        chks[en] = True
        rs += ew
        for next_edge in edge[en]:
            if chks[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)
print(rs)