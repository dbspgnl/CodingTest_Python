"""
# 노드 수 / 인접 정보 받기
# 인접 리스트 받기
4 2
4 2
3 1
= 4 2 3 1 or 3 4 1 2
# 두번째 예시
10 4
1 3
2 6
3 6
5 9
= 1 2 4 5 7 8 10 3 9 6
"""
from collections import deque
v,e = map(int, input().split())
eList = [[] for _ in range(v+1)]
indegree = [0]*(v+1)

for _ in range(e):
    s,e = map(int, input().split())
    eList[s].append(e)
    indegree[e] +=1

q = deque()
for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    ev = q.popleft()
    print(ev, end=" ")
    for nv in eList[ev]:
        indegree[nv] -=1
        if indegree[nv] == 0:
            q.append(nv)
