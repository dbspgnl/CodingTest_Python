# 현재 피로도 k, [던전 입장 피로도 조건, 피로도 소모량]이 주어질 때
# 가장 많이 던전을 돌 수 있는 횟수
def solution(k, dungeons):
    global answer, n, visited
    answer = 0
    n = len(dungeons)
    visited = [0]*n

    def dfs(k, cnt, dungeons):
        global answer
        if cnt > answer:
            answer = cnt
        for i in range(n):
            if k >= dungeons[i][0] and not visited[i]:
                visited[i] = 1
                dfs(k-dungeons[i][1], cnt+1, dungeons)
                visited[i] = 0

    dfs(k, 0, dungeons)
    return answer
print(solution(80, [[80,20],[50,40],[30,10]])) # 3