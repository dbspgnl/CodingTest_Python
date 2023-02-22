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
import sys
input = sys.stdin.readline
n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False]*n for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x):
    global cnt
    cnt +=1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny,nx)
cnt = 0
rs = []
for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt = 0
            dfs(j,i)
            rs.append(cnt)
rs.sort()
print(len(rs))
print("---")
for i in rs:
    print(i)
