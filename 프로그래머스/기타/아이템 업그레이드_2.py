# 만든 문제
# 턴당 200 골드 발생
# 아이템 업그레이드 하면 더 많은 골드 얻을 수 있음
# 시간 제한 주어지고, 업그레이드 비용 주어질 때
# 최대로 벌 수 있는 골드?
def solution(time, gold, upgrade):
    # answer = 0
    def dfs(remain_time, remain_gold, index):
        print(remain_gold)
        print(index)
        print(len(upgrade))
        print(upgrade[index])

        up = upgrade[index]
        cost = up[0]
        work = up[1]
        remain_time -= work
        remain_gold += remain_time * gold
        if remain_time * gold > cost:
            remain_gold -= cost
            # answer = remain_gold
            index += 1
            # if index >= len(upgrade):
            if remain_time <= 0:
                return remain_gold
            else:
                dfs(remain_time, remain_gold, index)
    return dfs(time, 0, 0)
    # return answer

# 시간, 골드, [[업그레이드 비용, 효율]]
print(solution(100,200, [[0,5], [1500,3],[3000,1]])) # 4100
print(solution(11, 1000, [[0, 5], [100, 4], [200, 3]]))  # 2700
