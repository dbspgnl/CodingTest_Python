def solution(clothes):
    # 1. 옷을 종류별로 구분
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) +1
    # 2. 입지 않는 경우를 추가함
    answer = 1
    for type in hash_map:
        answer *= hash_map[type] + 1
    # 3. 아무 종류 입지 않는 경우 제외
    return answer-1 # 6-1 =5

print(solution([["yellohat", "headgear"],["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))