import sys
input = sys.stdin.readline
INF = sys.maxsize
n = int(input())
m = int(input())
rs = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    rs[i][i] = 0 # 자기자신
for i in range(m):
    a,b,w = map(int, input().split())
    rs[a][b] = min(rs[a][b], w)
for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if rs[j][i] > rs[k][i] + rs[j][k]:
                rs[j][i] = rs[k][i] + rs[j][k]
for j in range(1, n+1):
    for i in range(1, n+1):
        if rs[j][i] == INF: print(0, end=" ")
        else: print(rs[j][i], end=" ")
    print()