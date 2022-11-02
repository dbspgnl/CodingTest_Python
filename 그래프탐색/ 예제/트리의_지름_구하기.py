"""
트리의 지름은 트리를 구성하는 노드 중 두노드 사이의 거리가 가장 긴 것이다.
= 임의의 노드에서 가장 긴 경로로 연결돼 있는 노드는 트리의 지름에 해당하는 두 노드 중에 하나
= 따라서 임의의 노드 중 가장 긴 노드를 구한 뒤 다시 해당 노드로 가장 긴 연결을 찾으면 됨
(1. 임의의 노드 / 2. 구한 노드로 다시 탐색)
3 1 2 4 3 -1 은 노드3과 1이 2거리, 4와는 거리3으로 연결되어 있다. -1는 종료
A 인접리스트로 가중치 처리를 위해 튜플(a,b)로 처리한다.
"""
from collections import deque

N = int(input()) # 노드의 개수
A = [[] for _ in range(N+1)] # 인접리스트 세팅
distance = [0]*(N+1)
visited = [False]*(N+1)

for _ in range(N): # 모든 노드 한 번씩 순회
    Data = list(map(int, input().split())) # 데이터 담기
    index = 0
    S = Data[index] # 스타트 노드 (첫번째 값의 맨 앞)
    index += 1
    while True:
        E = Data[index] #리스트에서 하나씩 빼오기
        if E == -1: # 빼온 값이 -1이면 종료
            break
        V = Data[index+1] # 거리값
        A[S].append((E,V)) # 노드와 거리를 한 쌍으로 처리
        index += 2 # 다음 노드는 노드,거리,노드,거리 이기 때문에

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True # 방문처리
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]: #지금 노드의 값들을 처리
            if not visited[i[0]]: #노드를 방문하지 않았다면
                visited[i[0]] = True # 방문처리
                queue.append(i[0]) # 큐에 처리할 노드로 추가
                # 큐에 삽입된 노드 거리 = 현재 노드의 거리 + 엣지의 가중치로 변경
                distance[i[0]] = distance[now_Node] + i[1]

BFS(1) #임의의 값 입력
Max = 1 # 최대값

# 최대값 찾는 로직
for i in range(2, N+1): # 1부터 시작했으니 나머지를 순회해서 처리
    if distance[Max] < distance[i]:
        Max = i # 찾은 노드가 최대값 노드

distance = [0]*(N+1)
visited = [False]*(N+1)
BFS(Max)
distance.sort()
print(distance[N])

"""
5
1 3 2 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
=11
"""