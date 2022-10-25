"""
엣지의 가중치가 10이하의 자연수.
그래프의 시작점에서 다른 노드로의 최단 경로
= 시작점이 있고 다른 모든 경로 탐색 = 다익스트라
= 엣지가 양수임으로 음수 처리하는 벨만포드는 사용하지 않는다.

"""

import sys
input = sys.stdin.readline
from queue import PriorityQueue # 큐 사용

V, E = map(int, input().split()) # 노드 개수 / 엣지 개수
K = int(input()) # 스타트 노드 번호
distance = [sys.maxsize] * (V+1) # 1부터 사용하기 위해서 v+1
visited = [False] * (V+1) # 방문 여부 체크 배열
myList = [[] for _ in range(V+1)] # 인접리스트
q = PriorityQueue() # 큐 생성

for _ in range(E): # 모든 엣지를 탐색
    u, v, w = map(int, input().split())
    myList[u].append((v,w)) # 인접리스트 값 넣어주기

q.put((0, K)) # 파이썬의 앞에 있는 수로 자동 정렬이 되기 때문에
# 거리 값을 넣음으로 최소 값 정렬을 할 수 있다.
distance[K] = 0 # 시작 노드의 엣지값은 0이다. (시작이기 때문)

while q.qsize() > 0: # 큐가 다 빌 때까지 반복
    current = q.get()
    c_v = current[1] # 1번 인덱스부터 사용하기 싶어서 V+1 했기 때문에 1부터 처리
    if visited[c_v]: continue # 이미 방문했으면 스킵
    visited[c_v] = True # 방문하지 않았으면 방문처리
    for tmp in myList[c_v]: # 현재 노드의 연결 엣지 정보는 여러 개 임으로 하나씩 확인한다.
        next = tmp[0] # 다음 노드 번호
        value = tmp[1] # 가중치 정보
        # 다음번 노드의 엣지값보다 현재 노드(의 엣지값) + 다음 노드로 가는 엣지 가중치이 더 작으면
        if distance[next] > distance[c_v] +value: # (초기값은 INF라서 처음은 무조건 바뀜)
            distance[next] = distance[c_v] + value # 해당 값으로 대체함
            # 가중치가 정렬 기준이므로 순서를 가중치, 목표 노드 순으로 우선순위 큐 설정
            q.put((distance[next], next)) # 거리값을 넣고, 노드를 넣음

for i in range(1, V+1):
    if visited[i]: print(distance[i])
    else: print("INF")

"""
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
"""