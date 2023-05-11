# 섬(노드) 갯수 n과 [시작, 끝, 비용] 배열이 주어질 때
# 모든 섬을 이어서 가장 작은 값? (최소신장트리)
import heapq
def solution(n, costs):
    answer = 0
    lenth = len(costs)
    eList = [[] for _ in range(n)] # 노드 0번부터
    chk = [False]*n
    for cost in costs:
        a,b,c = cost[0], cost[1], cost[2]
        eList[a].append([c,b])
        eList[b].append([c,a])
    heap = [[0,1]] # 시작점
    while heap:
        ew, en = heapq.heappop(heap)
        if chk[en] == False: # 현재 섬 방문x
            chk[en] = True # 방문처리
            answer += ew
            for nList in eList[en]:
                if chk[nList[1]] == False: # 다음 섬 방문x
                    heapq.heappush(heap, nList) # heap 추가
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4