from collections import deque
def solution(n, computers):
    def bfs(v):
        queue.append(v)
        while queue:
            i = queue.popleft()
            visited[i] = 1 # 방문처리
            for nv in range(n):
                if computers[i][nv] and not visited[nv]:
                    queue.append(nv)
    answer = 0
    queue = deque()
    l = len(computers)
    visited = [0 for _ in range(l)]
    for i in range(n): # 컴퓨터 번호(0 ~ n-1)
        if not visited[i]:
            bfs(i)
            answer +=1
    return answer

# 2차원 배열로 주어진다. n=3 : 3x3 / computer[i][i] =1 (자기 자신)
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) #2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) #1