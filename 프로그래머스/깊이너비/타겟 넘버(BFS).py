def solution(numbers, target):
    answer = [0]
    count = 0
    for num in numbers:
        temp = []
        for ans in answer: # 하나씩 꺼내서 양쪽 모두를 살핌 = BFS
            temp.append(ans + num) # 양수 트리
            temp.append(ans - num) # 음수 트리
        answer = temp # 트리를 모두 담음
    for ans in answer: # 따라서 2**n 만큼 answer에 담긴다.
        if ans == target:
            count += 1
    return count

print(solution([1, 1, 1, 1, 1], 3)) #5
print(solution([4, 1, 2, 1], 4)) #2

from collections import deque
def solution2(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0]) # 양수 초기화
    queue.append([-1*numbers[0],0]) # 음수 초기화
    while queue:
        temp, index = queue.popleft()
        index +=1
        if index < n: # 양수 음수 같이 하기 때문에 BFS
            queue.append([temp+numbers[index], index]) # 양수 큐
            queue.append([temp-numbers[index], index]) # 음수 큐
        else:
            if temp == target:
                answer +=1
    return answer

print(solution2([1, 1, 1, 1, 1], 3)) #5
print(solution2([4, 1, 2, 1], 4)) #2