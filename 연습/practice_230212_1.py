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
# x,y가 주어지고 맵이 주어지면
# 1로 된 길의 수와
# 길의 최대 길이

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]* m for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y,x): # queue 사용
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs += 1
                    q.append((ny,nx))
    return rs
cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt+=1
            maxv = max(maxv, bfs(j,i))
print(cnt)
print(maxv)