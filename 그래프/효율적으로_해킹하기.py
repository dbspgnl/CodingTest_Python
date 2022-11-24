"""
어떤 회사에는 신뢰하는 관계와 신뢰하지 않는 관계로 이루어진 N개의 컴퓨터가 있다.
컴퓨터의 개수 N과 신뢰 관계 엣지 개수 M이 주어진다.
단방향 신뢰 관계 요소를 모두 받아서 인접리스트에 넣고,
최대로 해킹할 수 있는 컴퓨터들를 찾는다.
여러 대의 컴퓨터 번호를 배열에 넣고 출력한다.
"""
# 백준: 1325
from collections import deque
N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
answer = [0]*(N+1)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_node = queue.popleft()
        for i in A[now_node]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1 # 신뢰 관계임으로 +1
                queue.append(i)

for _ in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

for i in range(1, N+1):
    visited = [False]*(N+1)
    BFS(i)

maxVal = 0
for i in range(1, N+1):
    maxVal = max(maxVal, answer[i])

for i in range(1, N+1):
    if maxVal == answer[i]:
        print(i, end=' ')

"""
5 4
3 1
3 2
4 3
5 3
= 1 2
"""