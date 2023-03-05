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
import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int, input().split())
eList = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

# 인접리스트
for _ in range(m):
    s,e = map(int, input().split())
    eList[s].append(e)
    indegree[e] += 1

# 덱 세팅
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i) # 자기 자신이 진입차수가 된다.

while q:
    en = q.popleft()
    print(en, end=' ')
    for nn in eList[en]:
        indegree[nn] -=1
        if indegree[nn] == 0:
            q.append(nn)
