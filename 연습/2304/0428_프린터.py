def solution(priorities, location):
    answer = 0
    queue = list(enumerate(priorities))
    while queue:
        first = queue.pop(0) # pop(0)은 앞에서부터
        if any(first[1] < q[1] for q in queue): # 지금 값보다 큰 값이 있다면
            queue.append(first) # 뒤로 보냄
        else:
            answer +=1 # 탐색 횟수
            if first[0] == location:
                break
    return answer

print(solution([2, 1, 3, 2],2)) #1
print(solution([1, 1, 9, 1, 1, 1],0)) #5