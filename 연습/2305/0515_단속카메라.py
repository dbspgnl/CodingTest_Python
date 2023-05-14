# [진입, 진출] 시점을 담은 배열이 배열로 담길 때,
# 모든 차량을 한 번은 찍도록 카메라 배치하려면 몇 개 필요한가?
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1]) # 진출로 정렬
    start = -30001 # 조건 (-3만~3만)
    for route in routes:
        if route[0] > start:
            answer += 1
            start = route[1] # 카메라 구간 초기화
    return answer

print(solution([[-20,-15],[-14,-5],[-18,-13],[-5,-3]])) #2