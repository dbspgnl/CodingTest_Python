# from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0]*bridge_length # 다리의 큐 상태
    while q:
        answer +=1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0]  <= weight: # 버틸 수 있음
                truck = truck_weights.pop(0) # 대기중인 트럭 앞
                q.append(truck) # 다리에 트럭 추가

            else:
                q.append(0) # 빈 값 추가
    return answer

print(solution(2,10,[7,4,5,6])) # 8
print(solution(100,100,[10])) # 101
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10])) # 110

"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    step = 0
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step
"""