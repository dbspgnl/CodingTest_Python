import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
rs = [[INF] * (n+1) for _ in range(n+1)] # 맵

for i in range(1, n+1): rs[i][i] = 0 # 자기 자신은 거리가 0
for i in range(m):
    a,b,c = map(int, input().split()) # a>b 비용c
    rs[a][b] = min(rs[a][b], c) # 최대가 INF이고 최소값을 담아둔다.

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if rs[j][i] > rs[j][k] + rs[k][i]: # 경유 비용이 더 적으면
                rs[j][i] = rs[j][k] + rs[k][i] # 갱신

for j in range(1, n+1):
    for i in range(1, n+1):
        if rs[j][i] == INF: print(0, end=' ')
        else: print(rs[j][i], end=' ')
    print()

