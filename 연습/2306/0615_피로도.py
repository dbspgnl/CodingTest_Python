# 현재 피로도 k, [던전 입장 피로도 조건, 피로도 소모량]이 주어질 때
# 가장 많이 던전을 돌 수 있는 횟수
answer = 0
N = 0
visited = []
def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt+1, dungeons)
            visited[j] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
print(solution(80, [[80,20],[50,40],[30,10]])) # 3