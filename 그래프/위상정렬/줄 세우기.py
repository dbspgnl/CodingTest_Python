"""
사람의 키 N과 비교할 횟수 M이 주어진다.
다음으로는 비교할 대상이 횟수만큼 주어진다.
앞에 키가 뒤에 키보다 더 앞에 서야 한다.
답이 여러 개라면 아무 순서대로 표기한다.
"""
# 위상정렬 문제
# 인접리스트를 받고, 진입 차수 리스트를 만든다.
# 진입차수 0을 찾아서 큐에 넣고 반복
from collections import deque
N, M = map(int, input().split())
A = [[] for _ in range(N+1)] # 0무시
indegree = [0]*(N+1)
for i in range(M): # 초기 세팅
    S, E = map(int, input().split())
    A[S].append(E)
    indegree[E] += 1 # 진입 차수 저장
queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
while queue: #위상 정렬 큐가 빌 때까지
    now = queue.popleft()
    print(now, end=' ')
    for next in A[now]: #next는 진입 차수값
        indegree[next] -= 1 #해당 차수 빼주기
        if indegree[next] == 0: # 진입 차수 0이면 반복
            queue.append(next)
"""
4 2
4 2
3 1
= 4 2 3 1 or 3 4 1 2
"""