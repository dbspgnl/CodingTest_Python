# DFS
n = int(input())
maps = [list(map(int, input().strip())) for _ in range(n)]
chks = [[False] * n for _ in range(n)]
rs = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny, nx = y + dy[k], x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
            if maps[ny][nx] == 1 and chks[ny][nx] == False:
                chks[ny][nx] = True
                dfs(ny, nx)
for j in range(n):
    for i in range(n):
        if maps[j][i] == 1 and chks[j][i] == False:
            chks[j][i] = True
            each = 0
            dfs(j,i)
            rs.append(each)
rs.sort()
print(len(rs))
for i in rs:
    print(i)
