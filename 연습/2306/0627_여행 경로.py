# 모든 공항을 지나는 순서 (모든 도시를 방문할 수 없는 경우는 없다)
from collections import defaultdict
def solution(tickets):
    path = [] # 여행 경로 최종 순서
    graph = defaultdict(list) # {'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
    for start, end in tickets:
        graph[start].append(end)
    for airport in graph.keys(): # key만 뽑아서 해당 키로 역정렬
        graph[airport].sort(reverse=True)
    # 탐색 시작
    stack = ["ICN"] # 시작
    while stack:
        top = stack.pop()
        if top not in graph or not graph[top]: # key가 없거나 key의 데이터가 없으면
            path.append(top)
        else:
            stack.append(top) # 다시 넣음 = 이어서 찾기 위해서
            stack.append(graph[top].pop()) # 해당 공항의 value을 빼면서 stack에는 추가
    return path[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]