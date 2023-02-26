"""
# 세로 # 가로
# 0벽 1길
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
= 4
9
# 길 그룹 수
# 가장 긴 길 크기
"""
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y,x):
    rs = 0
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        rs +=1
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

count = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            count +=1
            maxv = max(maxv, bfs(j,i))
print(count)
print(maxv)