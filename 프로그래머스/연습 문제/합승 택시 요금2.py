# n개의 정점, 시작점 s, 도착점a,b 가격 are
# 다익스트라 방법
import heapq
def solution(n, s, a, b, fares):
    inf = float('INF')
    answer = inf
    graph = [[] for _ in range(n + 1)]
    dist = [[]]

    # 다익스트라
    def dijkstra(start):
        res = [inf for _ in range(n+1)]
        res[start] = 0
        q = []
        heapq.heappush(q, (res[start], start)) # 노선과 가중치
        while q:
            result_x, x = heapq.heappop(q)
            for nn, nw in graph[x]:
                if res[nn] > result_x + nw:
                    res[nn] = result_x + nw
                    heapq.heappush(q, ([res[nn], nn]))
        return res

    # 그래프 처리
    for a,b,w in fares:
        graph[a].append([b,w])
        graph[b].append([a,w])

    # 수행
    for i in range(1, n+1):
        dist.append(dijkstra(i))

    # 결과
    for i in range(1, n+1):
        answer = min(answer, dist[s][i] + dist[i][a] + dist[i][b])
    return answer

print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))  # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
print(solution(6, 4, 5, 6,
               [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))  # 18

