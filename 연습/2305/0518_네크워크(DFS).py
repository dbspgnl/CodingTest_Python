# 2차원 배열 길이 n이 주어지고, 배열 값이 주어진다.
# 0은 비연결, 1은 연결 상태일 때, 연결된 네트워크의 수?
def solution(n, computers): # 재귀
    def dfs(i):
        visited[i] = 1 # 방문처리
        for v in range(n): # 탐색
            if computers[i][v] and not visited[v]: # 연결(1)이고 미방문
                dfs(v)
    answer = 0
    visited = [0] * len(computers)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer +=1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) #2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) #1