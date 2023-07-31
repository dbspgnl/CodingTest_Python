# n개의 집이 있다. 처음과 끝이 이어진 동그란 배치이다.
# 각 집에 값(money)가 주어질 때, 인접한 두 집을 털지 않고 최대값 구하기.

def solution(money):
    # 첫 집을 무조건 터는 경우
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, len(money)-1): # 세번째부터
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    # 마지막 집을 무조건 터는 경우
    dp2 = [0] * len(money)
    dp2[0] = 0 # i:0
    dp2[1] = money[1] # i:1
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])

    return max(max(dp1), max(dp2))

print(solution([1, 2, 3, 1])) # 4

'''
dp는 누적합을 넣는다. 
인접 조건에 의해서 3칸씩 묶어서 생각한다.
3번째 집은 인접하지 않는 1번과 같이 계산하게 되는데 (1 + 3)이 이전(2)랑 비교해서
더 큰 값을 dp에 갱신한다.
다만, 첫 집과 마지막 집이 이어졌기 때문에 둘 다 포함될 가능성이 있다.
따라서, 첫 집을 무조건 터는 경우와 마지막 집을 무조건 터는 경우 중에 최대값을 구한다.
'''