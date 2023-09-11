# 기능 구현
from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        today = 100 - progresses[i] + speeds[i] -1
        workng_day = today//speeds[i]
        queue.append(workng_day)
    while queue:
        cnt = 1
        first = queue.popleft()
        while queue and queue[0] <= first:
            cnt +=1
            queue.popleft()
        answer.append(cnt)

    return answer

# [진행된 양], [진행 속도]
print(solution([93, 30, 55],[1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])) # [1, 3, 2]