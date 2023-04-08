# 모든 요소가 참이면 all / 하나라도 참이면 any
# 첫번째 요소보다 더 우선순위가 하나라도 있으면

def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)]
    while queue: # (0,2)(1,1)(2,3)(3,2)
        first = queue.pop(0)
        # print(first)
        if any(first[1] < q[1] for q in queue): # 첫번째 우선순위보다 높은 순위가 있다면
            queue.append(first) # 뒤로 보냄
        else: # 그렇지 않으면 = 1순위임
            answer +=1
            if first[0] == location: # 내가 찾는 인덱스
                break
    return answer

print(solution([2, 1, 3, 2],2)) #1
print(solution([1, 1, 9, 1, 1, 1],0)) #5