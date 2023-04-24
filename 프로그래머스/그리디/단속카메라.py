def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # 배열의 인덱스로 정렬 방법
    start = -30001
    for route in routes:
        if route[0] > start: # 카메라 필요
            answer +=1
            start = route[1] # 마지막 경로부터 다시
    return answer

print(solution([[-20,-15],[-14,-5],[-18,-13],[-5,-3]])) #2