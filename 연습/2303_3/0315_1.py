"""
4 4
1 2 3
2 3 4
1 4 5
4 2 3
= 10
"""
# 최소 신장 트리: 모든 노드를 이어서 (음수 가능) 가중치 합이 가장 작은 값 찾는 알고리즘
import sys
input = sys.stdin.readline
import heapq
v,e = map(int, input().split())
eList = [[] for _ in range(v+1)]
chk = [False] * (v+1)

for i in range(e):
    a,b,w = map(int, input().split())
    eList[a].append([w,b])
    eList[b].append([w,a])

heap = [[0,1]]
rs = 0
while heap:
    ew, ev = heapq.heappop(heap)
    if chk[ev] == False:
        chk[ev] = True
        rs += ew
        for nList in eList[ev]:
            if chk[nList[1]] == False:
                heapq.heappush(heap, nList)
print(rs)