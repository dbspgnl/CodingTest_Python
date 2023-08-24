# n개의 정점, 시작점 s, 도착점a,b 가격 are
# 다익스트라 방법
import heapq
def solution(n, s, a, b, fares):
    inf = float('INF')
    answer = inf
    graph = [[] for _ in range(n + 1)]
    result = [[]]

    # 다익스트라
    def dijkstra(start):
        dist = [inf for _ in range(n+1)]
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (dist[start], start))
        while heap:
            ew, ev = heapq.heappop(heap)
            for nw, nv in graph[ev]:
                if dist[nv] > ew + nw:
                    dist[nv] = ew + nw
                    heapq.heappush(heap, [dist[nv], nv])
        return dist

    # 그래프 처리
    for node1,node2,w in fares:
        graph[node1].append([w,node2])
        graph[node2].append([w,node1])

    # 수행
    for i in range(1, n+1):
        result.append(dijkstra(i))

    # 결과
    for i in range(1, n+1):
        answer = min(answer, result[s][i] + result[i][a] + result[i][b])
    return answer

print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))  # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))  # 14
print(solution(6, 4, 5, 6,
               [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))  # 18

