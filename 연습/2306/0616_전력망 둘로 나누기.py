def dfs(node, visitied, aList):
    visitied[node] = True
    for nn in aList[node]:
        if not visitied[nn]:
            dfs(nn, visitied, aList)

def solution(n, wires):
    answer = n
    aList = [[] for _ in range(n+1)]
    for wire in wires:
        a,b = wire
        aList[a].append(b)
        aList[b].append(a)
    for wire in wires:
        a,b = wire
        aList[a].remove(b)
        aList[b].remove(a)
        visited = [False] * (n+1)
        dfs(1, visited, aList)
        count = visited.count(True) # true 갯수 = 방문 횟수
        differ = abs(count - (n-count)) # 한쪽이 정해지면 다른쪽도 정해짐
        answer = min(answer, differ)
        aList[a].append(b)
        aList[b].append(a)
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])) #3
print(solution(4, [[1,2],[2,3],[3,4]])) #0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])) #1