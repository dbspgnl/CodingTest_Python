from collections import Counter
from functools import reduce
def solution(clothes):
    # 1. 옷을 종류별로 구분
    counter = Counter([type for clothe, type in clothes]) # for문의 type으로만 리스트를 만들겠다.

    # 2. 입지 않는 경우를 추가함
    # acc, cur 파라미터를 전달하면 cur+1에 acc를 계속 곱한다.
    answer = reduce(lambda acc, cur: acc * (cur+1), counter.values(), 1)

    # 3. 아무 종류 입지 않는 경우 제외
    return answer-1

print(solution([["yellohat", "headgear"],["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))