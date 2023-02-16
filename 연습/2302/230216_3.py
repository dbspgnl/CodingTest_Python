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
# BFS는 큐를 이용해서 처리한다.

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False]*m for _ in range(n)]
dy = [1,0,-1,0]
dx = [0,1,0,-1]
def bfs(y,x):
    rs = 1 # 하나 카운팅하고 시작함(여기 진입했다는 말은 길이 있다는 뜻)
    q = [(y,x)] # 큐가 필요함
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex+dx[k]
            # 탐색 시작
            if 0<=ny<n and 0<=nx<m: # 맵 범위 넘어서면 안됨
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs +=1
                    q.append([ny, nx])
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