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

# NxN
# 맵 정보
# 체크리스트
# 카운팅
# 방향
# 결과 배열
n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False]*n for _ in range(n)]
result = []
each = 0
dy = [0,1,0,-1]
dx = [1,0,-1,0]
# dfs
def dfs(y,x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if map[ny][nx]==1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)
for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0 # 각 길의 길이 초기화
            dfs(j, i)
            result.append(each)
result.sort()
print(len(result))
for i in result:
    print(i)
# 탐색 시작

# 결과 표시