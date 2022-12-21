"""
도시 수 N과 도로 수 M이 주어진다.
다음으로 출발 도시 번호, 도착 도수 번호, 시간이 주어진다.
마지막 라인에 시작할 도시 번호와 종착할 도시 번호가 주어진다.
모든 도로를 통해서 종착 도시에 갈 때의 최소 시간과
이 시간까지 맞추기 위해서 여유 시간이 없이 통과하는 도로의 수를 구하기.
"""
# 백준: 1948
# 인접 리스트
# 역방향 인접 리스트
# 진입 차수 리스트
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())
A = [[] for _ in range(N+1)] # 0은 무시
reverseA = [[] for _ in range(N+1)] # 0은 무시
indegree = [0]*(N+1)
for i in range(M): #값 담기
    S, E, V = map(int, input().split())
    A[S].append((E, V))
    reverseA[E].append((S, V))
    indegree[E] += 1
startDosi, endDosi = map(int, input().split())
queue = deque()
queue.append(startDosi)
result = [0]*(N+1)
while queue: # 위상 정렬
    now = queue.popleft()
    for next in A[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now]+next[1])
        if indegree[next[0]] == 0:
            queue.append(next[0])
resultCount = 0
visited = [False]*(N+1)
queue.clear()
queue.append(endDosi)
visited[endDosi] = True
while queue: # 위상 정렬 reverse
    now = queue.popleft()
    for next in reverseA[now]:
        # 1분도 쉬지 않는 도로 체크
        if result[next[0]] + next[1] == result[now]:
            resultCount +=1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])
print(result[endDosi])
print(resultCount)
"""
7
9
1 2 4
1 3 2
1 4 3
2 6 3
2 7 5
3 5 1
4 6 4
5 6 2
6 7 5
1 7
= 12
5
"""