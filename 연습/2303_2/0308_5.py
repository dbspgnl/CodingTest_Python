"""
# 노드 수 / 인접 정보 받기
# 인접 리스트 받기
4 2
4 2
3 1
= 4 2 3 1 or 3 4 1 2
# 두번째 예시
5 4
1 4
4 3
3 2
2 5
= 1 4 3 2 5
"""
# 위상정렬
from collections import deque
n,m = map(int, input().split())
eList = [[] for _ in range(n+1)]
indegree = [0]*(n+1)

for i in range(m):
    s,e = map(int, input().split())
    eList[s].append(e)
    indegree[e] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    ev = q.popleft()
    print(ev, end=" ")
    for nv in eList[ev]:
        indegree[nv] -= 1
        if indegree[nv] == 0:
            q.append(nv)