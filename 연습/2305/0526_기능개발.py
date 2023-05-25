from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        queue.append((100 - progresses[i] + speeds[i] - 1) // speeds[i])
    while queue:
        cnt = 1
        top = queue.popleft()
        while queue and queue[0] <= top: # 큐가 있고, 첫번째 값이 top보다 작으면
            cnt +=1
            queue.popleft()
        answer.append(cnt)
    return answer

print(solution([93, 30, 55],[1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])) # [1, 3, 2]