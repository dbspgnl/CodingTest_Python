from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q  = deque([0]*bridge_length)
    # print(q)
    truck_weights.reverse()
    bridge_weight = 0 # 실시간 다리 하중
    while truck_weights:
        bridge_weight -= q.popleft()
        # print(q)
        answer +=1
        if truck_weights:
            if bridge_weight + truck_weights[-1]  <= weight: # 버틸 수 있음
                truck = truck_weights.pop() # 대기중인 트럭 앞
                q.append(truck) # 다리에 트럭 추가
                bridge_weight += truck # 실시간 하중 추가
            else:
                q.append(0) # 빈 값 추가
        else: # 대기중 트럭 없으면
            q.append(0) 
    return answer

print(solution(2,10,[7,4,5,6])) # 8
# print(solution(100,100,[10])) # 101
# print(solution(100,100,[10,10,10,10,10,10,10,10,10,10])) # 110