# 현재 피로도 k, [던전 입장 피로도 조건, 피로도 소모량]이 주어질 때
# 가장 많이 던전을 돌 수 있는 횟수
def solution(k, dungeons):
    global answer, n, visited
    answer = 0
    n = len(dungeons)
    visited = [0]*n

    def dfs(k, cnt):
        global answer
        if cnt > answer:
            answer = cnt
        for i in range(n):
            if dungeons[i][0] <= k and not visited[i]:
                visited[i] = 1
                dfs(k-dungeons[i][1], cnt+1)
                visited[i] = 0

    dfs(k, 0) # 현재 피로도, 횟수, 던전정보
    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3