# 첫번째 배열은 작업의 진행도와 순서
# 두번째 배열은 각 작업의 처리속도 (완료는 100)
# 결과: 각 배포할 때마다 몇개씩 배포하는가?
from collections import deque
def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        for day in range(1, 101):
            if p+(s*day) >= 100:
                queue.append(day)
                break
        # queue.append((100 - progresses[i] + speeds[i] - 1) // speeds[i])
    while queue:
        cnt = 1
        top = queue.popleft()
        while queue and queue[0] <= top:  # 이전 작업과 동시에 배포 가능한 작업들 카운트
            cnt += 1
            queue.popleft()
        answer.append(cnt)
    return answer

print(solution([93, 30, 55],[1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])) # [1, 3, 2]

"""
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
"""