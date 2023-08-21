# n개의 정점, 시작점 s, 도착점a,b 가격 are
# 플로이드 워셜 방법
import sys
def solution(n, s, a, b, fares):
    inf = sys.maxsize
    cost = [[inf] * (n+1) for _ in range(n+1)]
    answer = inf
    def fw(): # 플로이드-워셜 최소값 구하기
        for k in range(1, n+1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if i == j: cost[i][j] = 0 # 자기 자신
                    else:
                        cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])

    # 노선 처리
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
    fw() # 수행
    
    # 결과
    for i in range(1, n+1):
        answer = min(cost[s][i] + cost[i][a] + cost[i][b], answer)
    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) # 82
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])) # 14
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])) # 18

