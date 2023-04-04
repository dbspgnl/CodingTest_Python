def solution(clothes):
    answer = 1
    closet = {}
    for value, key in clothes:
        if key in closet:
            closet[key].append(value) # 기존 dict에 넣음
        else:
            closet[key] = [value] # 새로 만듬

    # print(closet)
    # {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}

    for key in closet.keys():
        answer *= (len(closet[key])+1)

    return answer-1 # 모두 안 입는 경우를 빼준다.

# def solution(clothes):
#     d = {}
#     for c in clothes:
#         if c[1] not in d:
#             d[c[1]] = 1
#         else:
#             d[c[1]] += 1
#     answer = 1
#     for v in d.values():
#         answer *= (v + 1)
#     return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) #5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) #3