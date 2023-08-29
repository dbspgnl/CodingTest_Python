# n개의 정점, 시작점 s, 도착점(a,b), 노선가격fares
def solution(n, s, a, b, fares):
    inf = float('INF')
    ans = inf
    cost = [[inf] * (n+1) for _ in range(n+1)]
    def _f_w():
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if i == j:
                        cost[i][j] = 0
                    else:
                        cost[i][j] = min(cost[k][j]+cost[i][k], [i][j])
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
    _f_w()

    for i in range(1, n+1):
        ans = min(cost[s][i]+cost[i][a]+cost[i][b], ans) # s > i > a,b
    return ans

print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))  # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
print(solution(6, 4, 5, 6,
               [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))  # 18