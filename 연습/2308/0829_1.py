from collections import deque
def solution(board):
    n = len(board)
    inf = float('INF')
    price = [[inf] * n for _ in range(n)]
    price[0][0] = 0 # 시작점
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    queue = deque()
    queue.append((0,0,0,5))
    def bfs():
        while queue:
            x,y,c,d = queue.popleft()
            # if x == n-1 and y == n-1: continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nd = i

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if board[nx][ny] == 1:
                    continue

                if d == 5:
                    nc = c + 100
                elif nd == d:
                    nc = c + 100
                else: nc = c + 600

                if nc <= price[nx][ny]:
                    price[nx][ny] = nc
                    queue.append((nx,ny,nc,i))
        return price[-1][-1]
    return bfs()

print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # 900
print(solution(
    [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0]]))  # 3800
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))  # 2100
print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]]))  # 3200