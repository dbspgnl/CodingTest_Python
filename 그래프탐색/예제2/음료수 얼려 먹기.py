"""
행 N과 열 M을 받는다.
그리고 2차원 그래프를 받는다.
0은 음료는 담는 구멍이고, 1은 막혀있다.
이때 0으로 된 그룹은 총 몇개인가?
"""
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)
"""
4 5
00110
00011
11111
00000
"""
