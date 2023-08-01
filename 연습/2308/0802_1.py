# BFS
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
chks = [[False] * m for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny, nx = ey + dy[k], ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and chks[ny][nx] == False:
                    chks[ny][nx] = True
                    rs +=1
                    q.append((ny,nx))
    return rs
cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if maps[j][i] == 1 and chks[j][i] == False:
            chks[j][i] = True
            cnt +=1
            maxv = max(maxv, bfs(j,i))
print(cnt)
print(maxv)

