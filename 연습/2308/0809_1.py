# 작업 번호 배열이 주어지고, 내 프린터 번호가 주어졌을 때, 내 프린트는 몇번째 출력되는가?
def solution(priorities, location):
    answer = 0
    queue = list(enumerate(priorities))
    while queue:
        first = queue.pop(0)
        if any(first[1] < q[1] for q in queue): # 다른 배열 중에 더 높은 값이 있다면
            queue.append(first) # 맨 뒤로
        else:
            answer +=1
            if first[0] == location: # 내 작업 번호(인덳)
                break
    return answer

print(solution([2, 1, 3, 2],2)) #1
print(solution([1, 1, 9, 1, 1, 1],0)) #5