"""
# 노드 수 / 엣지 수
# 1번노드가 2번노드에 몇 가중치로? (양방향)
# 시작은 1로
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
# 최소 신장 트리는 힙과 체크리스트를 이용해서 모든 간선을 최소로 이어서 그 값을 계산한다.

import sys
import heapq
input = sys.stdin.readline
n,e = map(int, input().split())
eList = [[] for _ in range(n+1)]
chk = [False]*(n+1)

for _ in range(e): # 양방향 처리
    a,b,w = map(int, input().split())
    eList[a].append([w,b])
    eList[b].append([w,a])

heap = [[0,1]]
rs = 0
while heap: # 힙 반복
    ew, en = heapq.heappop(heap)
    if chk[en] == False: # 만약 지금 확인하는 노드가 방문하지 않았다면
        chk[en] = True # 방문 체크하고
        rs += ew # 결과값을 누적한다 = MST
        for nList in eList[en]: # 다음 값을 찾고
            if chk[nList[1]] == False: # 그 노드가 방문하지 않으면
                heapq.heappush(heap, nList) # 힙에 추가한다
print(rs)
