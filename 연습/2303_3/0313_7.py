"""
# NxN 맵크기
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
= 3
7
8
9
# 그룹 개수
# 각 그룹별 크기
"""
# dfs
import sys
input = sys.stdin.readline
n = int(input())
maps = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False]*n for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    global count
    count += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if maps[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny,nx)
count = 0
rs = []
for j in range(n):
    for i in range(n):
        if maps[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            count = 0
            dfs(j,i)
            rs.append(count)
print(len(rs))
rs.sort()
print("---")
for i in rs:
    print(i)
