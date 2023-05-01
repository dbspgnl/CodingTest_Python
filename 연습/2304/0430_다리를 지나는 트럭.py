# 다리의 길이와 견딜 수 있는 무게, 트럭의 각 무게 배열이 주어진다.
# 초당 다리 한 칸을 간다면 모든 트럭이 건너는 최소 시간
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q  = [0]*bridge_length # 다리 큐
    while q:
        answer +=1 # 최초 카운팅
        q.pop(0) # 맨앞
        if truck_weights: # 트럭이 있고
            # 이미 다리 위의 트럭 + 신규 트럭이 무게보다 낮으면 = 건널 수 있음
            if sum(q) + truck_weights[0] <= weight:
                truck = truck_weights.pop(0) # 트럭 배열에 맨앞 제거하고
                q.append(truck) # 그 트럭을 다리 큐에 올림
            else:
                q.append(0) # 다리 큐에 빈값 추가
    return answer

print(solution(2,10,[7,4,5,6])) # 8
print(solution(100,100,[10])) # 101
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10])) # 110