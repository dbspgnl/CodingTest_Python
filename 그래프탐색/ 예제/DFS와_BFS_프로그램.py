"""
DFS와 BFS로 각각 구현하고 결과를 출력한다.
= DFS / BFS
N(노드의 개수) / M(엣지 개수) / Start(시작노드)
A(인접리스트)
"""
# 구조 세팅
from collections import deque
N, M, Start = map(int, input().split())
A = [[] for _ in range(N+1)]

# 인접리스트 세팅
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
# 인접리스트 정렬
for i in range(N+1):
    A[i].sort()

# DFS
def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]: # DFS는 재귀식으로 처리
        if not visited[i]:
            DFS(i)

visited = [False]*(N+1)
DFS(Start)

# BFS
def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True # 방문처리
    while queue: # 큐에 있는 내용이 없을 때까지
        now_Node = queue.popleft()
        print(now_Node, end =' ')
        for i in A[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i) # 방문한 노드 큐에 담기

print() # 한 칸 내리기
visited = [False]*(N+1) # 초기화
BFS(Start)

"""
4 5 1
1 2
1 3
1 4
2 4
3 4
=1 2 4 3
1 2 3 4

5 5 3
5 4
5 2
1 2
3 4
3 1
=3 1 2 5 4
3 1 4 2 5
"""