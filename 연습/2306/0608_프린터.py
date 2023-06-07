def solution(priorities, location):
    answer = 0
    queue = list(enumerate(priorities))
    while queue:
        first = queue.pop(0)
        if any(first[1] < q[1] for q in queue):
            queue.append(first) # 우선 순위 더 높은 게 있으면 뒤로 보냄
        else:
            answer +=1 # count
            if first[0] == location: break
    return answer

print(solution([2, 1, 3, 2],2)) #1
print(solution([1, 1, 9, 1, 1, 1],0)) #5