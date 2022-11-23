"""
N개의 도시와 M개의 도로, 찾고자 하는 최단거리 K, 시작도시 X가 주어진다.
모든 도시 간의 거리는 1이다.
이후 이어진 도시 간의 정보를 쌍을 입력 받는다.
이때, 찾고자 하는 K길이의 도시가 있다면 배열로 출력하고 없으면 -1을 출력한다.
"""
# 백준: 18352
from collections import deque
N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [-1]*(N+1) # 거리 값과 방문 여부를 동시에 체크
answer = []

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1 # 시작할 때 거리를 0으로 맞추기 위함
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node]+1 # 뎁스가 깊어질 수록 +1
                queue.append(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)
BFS(X)

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)

"""
4 4 2 1
1 2
1 3
2 3
2 4
= 4
4 3 2 1
1 2
1 3
1 4
=-1
"""