# [조건, 소모]에서 조건이 해당한다고 무조건 가면 안됨
# 소모가 낮다고 무조건 가면 조건에 걸림
# 두 차이가 적을 수록 남은 피로도가 많음
"""
def solution(k, dungeons):
    prior = list(i-j for i,j in dungeons)
    prior = list(enumerate(prior))
    prior = [(i[1],i[0]) for i in prior]
    prior.sort(reverse=True)
    count = 0
    for i in range(len(dungeons)):
        idx = prior[i][1]
        if k >= dungeons[idx][0]:
            k -= dungeons[idx][1]
            count += 1
    return count
"""
def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0
answer = 0
N = 0
visited = []
def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer
print(solution(80, [[80,20],[50,40],[30,10]])) # 3
print(solution(80, [[40,40], [40,40]]))