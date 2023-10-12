# 만든 문제
# 턴당 200 골드 발생
# 아이템 업그레이드 하면 더 많은 골드 얻을 수 있음
# 시간 제한 주어지고, 업그레이드 비용 주어질 때
# 최대로 벌 수 있는 골드?
import math
def solution(time, gold, upgrade):
    answer:int = 0
    update_cost = 0
    for i in range(len(upgrade)):
        work = upgrade[i][1]
        cost = upgrade[i][0]
        update_cost += upgrade[i][0]
        now_gold = 0
        now_time = time
        while now_time <= 0:
            now_time = now_time - work
            now_gold = now_gold + gold
        update_cost += upgrade[i][0]
        turn = math.ceil(update_cost / gold)
        remain = (turn * gold) - update_cost

        time = time - (turn*upgrade[i-1][1]) # 남은 시간 갱신
        answer = max(answer, ((time//work)*gold) + remain)
    return answer

# 시간, 골드, [[업그레이드 비용, 효율]]
print(solution(100,200, [[0,5], [1500,3],[3000,1]])) # 4100
print(solution(11, 1000, [[0, 5], [100, 4], [200, 3]]))  # 2700
