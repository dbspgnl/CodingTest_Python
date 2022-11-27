"""
1이상 200이하의 크기의 물통 3개가 있다. 마지막 물통은 가득 차있다.
1번 물통이 비어 있을 때의 3번 물통이 담긴 물의 양의 경우의 수를 모두 구하시오.
- 한 번 체크한 경우의 수는 스킵한다.
- 세 개의 물통에서 한 물통 기준 경우의 수는 6개이다. (다음번 처리)
- 각물통 정보
- 방문 리스트
- 정답 리스트
"""
# 백준: 2251
from collections import deque
Sender = [0, 0, 1, 1, 2, 2] # 각각 0번 물통, 1번 물통, 2번 물통
Receiver = [1, 2, 0, 2, 0, 1] # 사방진 표시랑 같은 역할
now = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)]
answer = [False] * 201
# BFS
def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    answer[now[2]] = True
    while queue:
        now_node = queue.popleft()
        A = now_node[0]
        B = now_node[1]
        C = now[2] - A - B # 현재 물양에서 A와 B를 뺌
        for k in range(6):
            next = [A, B, C]
            next[Receiver[k]] += next[Sender[k]]
            next[Sender[k]] = 0
            if next[Receiver[k]] > now[Receiver[k]]: # 물이 넘칠 때
                next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]] # 남는 물 다시 채움
                next[Receiver[k]] = now[Receiver[k]] # 대상 물통
            if not visited[next[0]][next[1]]: # A와B 물양으로 방문 리스트 체크
                visited[next[0]][next[1]] = True
                queue.append((next[0],next[1]))
                if next[0] == 0: # A 물양이 0일때 C물 변수 저장
                    answer[next[2]] = True
BFS()
for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')
"""
8 9 10
= 1 2 8 9 10
"""