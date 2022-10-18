"""
1. 아이디어
- 2중 for문을 돌면서 => 값 1 && 방문X => BFS
- BFS 돌면서 그림 개수 +1, 최대값을 갱신

2. 시간복잡도
- BFS : O(V+E)
- V : 500 * 500
- E : 4 * 500 * 500
- V+E : 5 * 250000 = 100만 < 2억 : 가능

3. 자료구조
- 그래프 전체 지도: int[][]
- 방문 : bool[][]
- Queue(BFS)
"""

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

# 우, 하, 좌, 상
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def bfs(y,x):
    rs = 1 # 전체 크기 결과 (1로 이어진 크기)
    q = [(y,x)] # 큐
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m: # 맵 범위에서 벗어나지 않도록 처리
                if map[ny][nx] == 1 and chk[ny][nx] == False: # 맵이 1이면서 방문한 적 없는
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs

cnt = 0 #
maxv = 0 # 최고값 갱신을 위한 변수
for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            cnt += 1
            maxv = max(maxv, bfs(j,i))
print(cnt)
print(maxv)

"""
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
= 4
9
"""