# 피로도
def solution(k, dungeons):
    global answer, n, visited, cnt
    answer = 0
    n = len(dungeons)
    visited = [0]*n
    cnt = 0
    def dfs(k):
        global answer, cnt
        if cnt > answer:
            answer = cnt
        for i in range(n):
            if dungeons[i][0] >= k and not visited[i]:
                visited[i] = 1
                cnt+=1
                dfs(k-dungeons[i][1])
                visited[i] = 0
    dfs(k)
    return answer

print(solution(80, [[80, 20], [50, 40], [30, 10]]))  # 3