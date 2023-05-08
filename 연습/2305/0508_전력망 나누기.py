# n개의 송전탑과 간선 정보가 트리 형태로 주어질 때,
# 특정 간선을 잘라서 송전탑이 최대한 비슷하게 하려면,
# 그 양쪽 차이가 가장 작은 값 구하기

from collections import deque
import sys
inf = sys.maxsize

def bfs(node, tree, visited, wire, cnt):
    queue = deque()
    queue.append([node, tree, visited, wire])
    visited[node] = True # 방문 처리
    while queue:
        node, tree, visited, wire = queue.popleft()
        cnt +=1
        for i in tree[node]:
            # 현재 노드와 트리에서 순회하면서 찾는 노드가 같지 않으면
            if not ((node == wire[0] and i == wire[1]) or (node == wire[1] and i == wire[0])):
                if not visited[i]:
                    visited[i] = True
                    queue.append([i, tree, visited, wire])
    return cnt

def solution(n, wires):
    answer = inf # 1e9
    tree = [[] for _ in range(n + 1)]
    for wire in wires: # 간선 처리
        a,b, = wire
        tree[a].append(b)
        tree[b].append(a)
    for wire in wires:
        visited = [False]*(n+1) # 방문도 초기화 해줌
        temp = [] # 카운팅 완료 후 배열로 정보 담음 (쪼개진 a,b 트리)
        for i in range(1, n+1):
            if not visited[i]: # 방문하지 않았으면 탐색
                cnt = bfs(i, tree, visited, wire, 0) # 노드, 전체트리, 방문배열, 간선, 카운팅
                temp.append(cnt)
        answer = min(answer, abs(temp[0] - temp[1])) # 배열 두 개일때 최소값 하나로 만듬
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) #3
# print(solution(4, [[1,2],[2,3],[3,4]])) #0
# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) #1