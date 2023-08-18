# 최단 거리 문제. 다만, 코너를 최소화 해야한다. (0은 길, 1은 벽)
# 직선 = 100원, 코너 = 500원 소요. 최단 거리의 가격?
from collections import deque
import sys
def solution(board):
    n = len(board)
    price = [[sys.maxsize] * n for _ in range(n) ]
    price[0][0] = 0 # 시작점
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    queue = deque()
    queue.append((0,0,0,5)) # 시작x, 시작y, 시작cost, 시작 방향
    def bfs():
        while queue:
            x,y,c,d = queue.popleft()
            if x == n-1 and y == n-1: # 마지막 위치
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nd = i

                # 맵 범위 처리
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == 1:
                    continue

                # 방향에 따른 가격 처리
                if d==5:
                    nc = c + 100
                elif nd == d:
                    nc = c + 100
                else:
                    nc = c + 600

                if nc <= price[nx][ny]:
                    price[nx][ny] = nc
                    queue.append((nx,ny,nc,i))
        return price[-1][-1]
    return bfs()

print(solution([[0,0,0],[0,0,0],[0,0,0]])) # 900
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])) # 3800
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])) # 2100
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])) # 3200