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
# 길 크기
"""
# BFS는 queue를 사용한다.
import sys
n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y,x):
    q = [(y,x)]
    rs = 1
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if chk[ny][nx] == False and map[ny][nx] == 1:
                    chk[ny][nx] = True
                    rs +=1
                    q.append((ny,nx))

    return rs
count = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if chk[j][i] == False and map[j][i] == 1:
            chk[j][i] = True
            count +=1
            maxv = max(maxv, bfs(j,i))
print(count)
print(maxv)