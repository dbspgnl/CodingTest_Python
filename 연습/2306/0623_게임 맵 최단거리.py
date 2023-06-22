# 0은 벽이고, 1은 길이다. 가장 짧은 길을 찾고, 없으면 -1
# 시작점은 0,0 끝점은 반대편
from collections import deque
def solution(maps):
    n = len(maps[0]) # x
    m = len(maps) # y
    count = 1
    queue = deque()
    queue.append([0,0,count])
    maps[0][0] = 0 # 방문 처리
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    while queue:
        x,y,count = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx == m-1 and ny == n-1: # 도착
                return count+1
            if 0 <= nx < m and 0 <= ny < n:
                if maps[nx][ny] != 0:
                    maps[nx][ny] = 0
                    queue.append([nx,ny,count+1])
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) # 11
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) # -1