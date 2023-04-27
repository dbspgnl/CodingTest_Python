from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN", ["ICN"], [])) # 공항명, 경로, 경유여부
    while q:
        airport, path, used = q.popleft()
        if len(used) == len(tickets): # 정답 담기
            answer.append(path)
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used: # 첫번째 티켓이 현재 공항이고, 경유한적이 없으면
                q.append((ticket[1], path+[ticket[1]], used+[idx])) #

    return answer[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])) # ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])) # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]