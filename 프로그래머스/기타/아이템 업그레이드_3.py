# 첫번째 업그레이드 단순 소모
def solution1(time, gold, upgrade):
    remain_gold = 0
    while time > 0:
        # global remain_gold
        work = upgrade[0][1]
        time -= work
        remain_gold += gold
    return remain_gold
    # return answer

# 시간, 골드, [[업그레이드 비용, 효율]]
print(solution1(100,200, [[0,5], [1500,3],[3000,1]])) # 4100
print(solution1(11, 1000, [[0,5], [100,4], [200,3]]))  # 2700

print("-----------------------------------------")

# 첫번째로 했을 때 비용과 두번째 했을 때 비용을 계산
def solution2(time, gold, upgrade):
    def dfs(time, gold, work):
        remain_gold = 0
        while time > 0:
            time -= work
            remain_gold += gold
        return remain_gold
    return dfs(time, gold, upgrade[0][1])
    # return answer

# 시간, 골드, [[업그레이드 비용, 효율]]
print(solution2(100,200, [[0,5], [1500,3],[3000,1]])) # 4100
print(solution2(11, 1000, [[0,5], [100,4], [200,3]]))  # 2700

'''
new_array = []
    sum_upgrade_cost = 0
    remain_time = time
    for i in range(len(upgrade)):
        cost = upgrade[i][0]
        sum_upgrade_cost += cost
        # 몇턴만에 업그레이드를 채울 수 있는가?
        turn = (sum_upgrade_cost//gold) +1
        work = upgrade[i][1]
        remain_time -= work*turn
'''