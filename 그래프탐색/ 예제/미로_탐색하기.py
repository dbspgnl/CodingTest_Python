"""
2차원 배열에서 1이면 이동, 0이면 막힘일 때 (0,0)에서 (n,m)까지 최소 이동 칸 수를 구하라.
N과 M은 100으로 매우 작다.
방향이 존재하기 때문에 4방향 처리를 넣어줘야 한다.
전형적인 BFS
"""
from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split()) # 미로 만들기
A = [[0]*M for _ in range(N)] # 거리 계산 배열
visited = [[False]*M for _ in range(N)] # 방문 체크 배열

for i in range(N): # 미로 생성
    numbers = list(input()) # 리스트로 input 담기
    for j in range(M):
        A[i][j] = int(numbers[j]) # 줄마다 input 값 심어주기

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 <= x < N and 0 <= y < M: # 범위 제한
                if A[x][y] != 0 and not visited[x][y]: # 진입 불가 및 방문 여부 체크
                    visited[x][y] = True # 방향 탐색 시 방문 표시
                    A[x][y] = A[now[0]][now[1]] + 1 # 현재 값에 뎁스 추가 (이동 거리 추가)
                    queue.append((x,y))

BFS(0,0)
print(A[N-1][M-1])

"""
4 6
101111
101010
101011
111011
= 15
4 6
110110
110110
111111
111101
= 9
"""