"""
# 도시 개수
# 버스 개수
# 버스 노선 인접리스트
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
=0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
# y>x으로 가는 비용을 2차원 배열로 표시함
"""
# 플로이드 워셜: 음수 가중치도 최단 거리를 구할 수 있는 알고리즘
import sys
input = sys.stdin.readline
inf = sys.maxsize
n = int(input())
m = int(input())
rs = [[inf] * (n+1) for _ in range(n+1)]

for i in range(1, n+1): rs[i][i] = 0
for i in range(m):
    a,b,w = map(int, input().split())
    rs[a][b] = min(rs[a][b], w)

for k in range(1, n+1):
    for j in range(1, n+1):
        for i in range(1, n+1):
            if rs[j][i] > rs[j][k] + rs[k][i]:
                rs[j][i] = rs[j][k] + rs[k][i]

for j in range(1, n+1):
    for i in range(1, n+1):
        if rs[j][i] == inf: print(0, end=" ")
        else: print(rs[j][i], end=" ")
    print()