def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    # print(routes) 나가는 시점 기준으로 정렬
    start = -30001 # 매우 작은 수
    for route in routes:
        if route[0] > start:
            answer += 1
            start = route[-1]
    return answer

print(solution([[-20,-15],[-14,-5],[-18,-13],[-5,-3]])) #2