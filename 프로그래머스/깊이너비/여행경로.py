# 모든 공항을 지나는 순서 (모든 도시를 방문할 수 없는 경우는 없다)
from collections import defaultdict
def solution(tickets):
    path = []
    graph = defaultdict(list)
    for (start, end) in tickets:
        graph[start].append(end)
    # print(graph)
    for airport in graph.keys():
        graph[airport].sort(reverse=True)
    stack = ["ICN"] # 시작 공항 고정
    while stack:
        top = stack.pop()
        if top not in graph or not graph[top]: # top이 그래프x or top으로 시작하는게 없다면
            path.append(top)
        else: # top의 도착점에서 마지막 지점을 가져와 스택
            stack.append(top)
            stack.append(graph[top].pop())
    return path[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]