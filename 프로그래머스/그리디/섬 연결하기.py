import heapq
def solution(n, costs):
    answer = 0
    l = len(costs)
    eList = [[] for _ in range(n)]
    chk = [False] * n
    for cost in costs:
        a,b,c = cost[0], cost[1], cost[2]
        eList[a].append([c,b])
        eList[b].append([c,a])
    heap = [[0,1]]
    while heap:
        ew, en = heapq.heappop(heap)
        if chk[en] == False:
            chk[en] = True
            answer += ew
            for nList in eList[en]:
                if chk[nList[1]] == False:
                    heapq.heappush(heap, nList)
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4