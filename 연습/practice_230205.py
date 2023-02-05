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
# 길 몇 개인지
# 길 길이

import sys
input = sys.stdin.readline
n,m = map(int, input().split()) # y,x
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y,x):
    rs = 1
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            # 맵이 벗어나면 안됨
            if 0<=ny<n and 0<=nx<m:
                # 1이면 길이고, 방문한적 없어야함
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    # 결과+1
                    rs+=1
                    # 방문 처리
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs
cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))
print(cnt)
print(maxv)