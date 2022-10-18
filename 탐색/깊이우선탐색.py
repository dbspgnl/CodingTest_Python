"""


"""

N = int(input())
# _는 실제로 사용하지 않고 반복할 때 사용
# 따라서 N만큼 시행 후 다시 N만큼 시행할 때 유용하다
map = [list(map(int, input().strip())) for _ in range(N)]
chk = [[False] * N for _ in range(N)]
result = [] # 결과를 담는 배열
each = 0
# 우, 하, 좌, 상
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y, x):
    global each # 전역 변수 처리
    each += 1
    for k in range(4): # 4방향이라 4번씩 처리한다.
        ny = y + dy[k] # y좌표
        nx = x + dx[k] # x좌표
        if 0<=ny<N and 0<=nx<N: # 맵에서 벗어나지 않아야 함
            if map[ny][nx] == 1 and chk[ny][nx] == False: # 1이 있는 곳이어야 하며, 들린 적이 없어야 한다.
                chk[ny][nx] = True # 체크맵 true 처리
                dfs(ny, nx)

for j in range(N):
    for i in range(N):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)


"""
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
"""