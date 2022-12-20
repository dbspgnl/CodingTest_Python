"""
건물의 종류가 N이 주어진다.
그리고 그 다음줄 부터 N번 건물 종류에 대한 건설 시간과 선행 건물 번호가 주어진다.
N번째 건물의 건물 번호가 N이 된다.
이 때 각 건물이 완성되는 최소 시간을 출력.
-1은 입력 종료.
"""
# 백준: 1516
# 위상정렬 문제
# 인접 리스트
# 진입 차수 리스트
# 건설 시간 리스트
from collections import deque
N = int(input())
A = [[] for _ in range(N+1)] # 0무시
indegree = [0]*(N+1)
selfBulid = [0]*(N+1)
for i in range(1, N+1):
    inputList = list(map(int, input().split()))
    selfBulid[i] = inputList[0]
    index = 1
    while True: # 인접리스트 채우기
        preTemp = inputList[index]
        index += 1
        if preTemp == -1:
            break
        A[preTemp].append(i)
        indegree[i] += 1 # 진입 차수
queue = deque()
for i in range(1, N+1):
    if indegree[i] == 0: # 0을 찾아서 큐 넣기
        queue.append(i)
result = [0]*(N+1)
while queue: # 큐가 빌 때까지 위상정렬
    now  = queue.popleft()
    for next in A[now]:
        indegree[next] -= 1
        # 건설 시간 업데이트
        result[next] = max(result[next], result[now] + selfBulid[now])
        if indegree[next] == 0:
            queue.append(next)
# 출력
for i in range(1, N+1):
    print(result[i] + selfBulid[i])
"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
=10
20
14
18
17
"""