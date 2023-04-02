def solution(nums):
    can_pick = int(len(nums)/2) # 항상 짝수
    set_nums = list(set(nums))
    result = []
    for i in range(can_pick):
        if i >= len(set_nums): break
        result.append(set_nums[i])
    return len(result)

print(solution([3,1,2,3])) #2
print(solution([3,3,3,2,2,4])) #3
print(solution([3,3,3,2,2,2])) #2

"""
def solution(nums
    return min(len(nums)/2, len(set(nums)))
"""