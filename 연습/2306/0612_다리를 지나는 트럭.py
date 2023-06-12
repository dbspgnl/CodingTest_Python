# 다리의 길이와 견딜 수 있는 무게, 트럭의 각 무게 배열이 주어진다.
# 초당 다리 한 칸을 간다면 모든 트럭이 건너는 최소 시간
def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length
    while q:
        answer +=1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                q.append(truck)
            else:
                q.append(0)
    return answer

print(solution(2, 10, [7, 4, 5, 6]))  # 8
print(solution(100, 100, [10]))  # 101
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))  # 110