# 트리 구조의 특정 간선을 제거해서 두 개로 나눌 때, 두 트리의 노드 갯수의 차이를 최소화 하는 문제
def dfs(node, visitied, aList):
    visitied[node] = True
    for nn in aList[node]:
        if not visitied[nn]:
           dfs(nn, visitied, aList)

def solution(n, wires):
    answer = n # 최대값 세팅
    aList = [[] for _ in range(n+1)]
    for wire in wires:
        a,b = wire # 양방향 인접리스트 세팅
        aList[a].append(b)
        aList[b].append(a)
    for wire in wires:
        a,b = wire
        aList[a].remove(b) # 끊고 탐색해서 계산해본다
        aList[b].remove(a)
        visited = [False] * (n+1) # 방문 초기화
        dfs(1, visited, aList)
        count = visited.count(True) # 방문 횟수가 한쪽 길이가 된다
        differ = abs(count - (n-count))
        answer = min(answer, differ)
        aList[a].append(b) # 다시 연결 상태에서 탐색하기 위해 붙여준다
        aList[b].append(a)
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) #3
print(solution(4, [[1,2],[2,3],[3,4]])) #0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) #1


"""
# 제일 짧은 계산식
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))
    return ans
"""

"""
# BFS로 푼 문제 
from collections import deque

def bfs(node, tree, visited, wire, cnt):
    queue = deque()
    queue.append([node, tree, visited, wire])
    visited[node] = True

    while queue:
        node, tree, visited, wire = queue.popleft()
        cnt += 1

        for i in tree[node]:
            if not ((node == wire[0] and i == wire[1]) or (node == wire[1] and i == wire[0])):
                if not visited[i]:
                    visited[i] = True
                    queue.append([i, tree, visited, wire])

    return cnt


def solution(n, wires):
    answer = 1e9
    tree = [[] for _ in range(n + 1)]

    for wire in wires:
        a, b = wire
        tree[a].append(b)
        tree[b].append(a)

    for wire in wires:
        visited = [False] * (n + 1)
        temp = []
        for i in range(1, n + 1):
            if not visited[i]:
                cnt = bfs(i, tree, visited, wire, 0)
                temp.append(cnt)

        answer = min(answer, abs(temp[0] - temp[1]))

    return answer
"""