# 다이아몬드, 철, 돌 곡갱이가 있다. 본래 피로도 1소모되지만, 철 > 다이아: 5, 돌 > 철: 5, 돌 > 다이아: 25가 소모된다.
# 사용할 수 있는 곡갱이의 수와 배열은 [다이아, 철, 돌] 순으로 되어 있다. (빈 배열은 없다) 0<= n <=5
# **한 번 캐기 시작하면 5개를 연속으로 캔다
# 자원은 5<= n <=50 길이이며 문자열로 구분된다.
def solution(picks, minerals):
    answer = 0
    minerals = [minerals[i:i+5] for i in range(0, len(minerals), 5)] # 5개씩 끊어서
    costs = []
    for mineral in minerals:
        cost = [0,0,0] # 다이아, 철, 돌
        for mine in mineral:
            if mine == "diamond":
                cost[0] += 1
                cost[1] += 5
                cost[2] += 25
            elif mine == "iron":
                cost[0] += 1
                cost[1] += 1
                cost[2] += 5
            else:
                cost[0] += 1
                cost[1] += 1
                cost[2] += 1
        costs.append(cost)

    for cost in costs:
        if picks[0] > 0:
            picks[0] -=1
            answer += cost[0]
            continue
        elif picks[1] > 0:
            picks[1] -= 1
            answer += cost[1]
            continue
        elif picks[2] > 0:
            picks[2] -= 1
            answer += cost[2]
            continue
    return answer

print(solution([1, 3, 2],	["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])) #12
print(solution([0, 1, 1],	["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])) #50
