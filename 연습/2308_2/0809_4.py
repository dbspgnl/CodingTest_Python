# 0은 벽이고, 1은 길이다. 가장 짧은 길을 찾고, 없으면 -1
# 시작점은 0,0 끝점은 반대편
from collections import deque
def solution(maps):
    m = len(maps[0])
    n = len(maps)
    count =1
    queue = deque()
    queue.append([0,0,count])
    maps[0][0] = 0
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    while queue:
        y,x,count = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx == m-1 and ny == n-1:
                return count+1
            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] != 0:
                    maps[ny][nx] = 0
                    queue.append([ny, nx, count+1])
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1