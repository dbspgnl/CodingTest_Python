# 위상 정렬
# 앞뒤로 빼기 위해서 deque 사용
from collections import deque
n,m = map(int, input().split())
a = [[] for _ in range(n+1)]
indegree = [0]*(n+1) # 진입차수 리스트
for i in range(m):
    s,e = map(int, input().split())
    a[s].append(e)
    indegree[e] += 1 # e는 s가 들어옴으로 진입 차수 증가
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i) # 진입 차수 없음 = 시작점
while q:
    now = q.popleft()
    print(now, end=' ')
    for next in a[now]:
        indegree[next] -= 1 # 다음 노드의 차수를 -1 줄여주면서 시작
        if indegree[next] == 0:
            q.append(next)