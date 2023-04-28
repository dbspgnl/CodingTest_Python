from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        # 100% - 진행된 양 + 오늘 진행 양 - 1를 진행 양로 나눈 몫: 앞으로 걸릴 일 수
        queue.append((100 - progresses[i] + speeds[i] -1) // speeds[i]) # ([7, 3, 9])
    while queue:
        cnt = 1
        top = queue.popleft() # 7, 3, 9
        while queue and queue[0] <= top: # top은 첫번째, queue[0]은 남은 것들 중에 첫번째
            # print("top:", top) # 7
            # print("queue[0]:", queue[0]) # 3
            cnt +=1 # 즉, 남은 것들 중에 현재보다 작은 것들이 있다면 (끝난 작업이므로 카운팅)
            queue.popleft() # 그 작업도 처리한 걸로 하기 위해서 대기에서 제외
        answer.append(cnt)
    print(queue)
    return answer

print(solution([93, 30, 55],[1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])) # [1, 3, 2]