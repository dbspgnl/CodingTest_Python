# 주어진 수열이 등차/등비 수열이라면 마지막 다음 수를 추론해라.

def solution(common):
    for n1, n2, n3 in zip(common, common[1:], common[2:]):
        if n2 + (n2 - n1) == n3:
            return int(common[-1] + (n2 - n1))
        elif n2 * (n2 / n1) == n3:
            return int(common[-1] * (n2 / n1))
print(solution([1,2,3,4])) # 5
print(solution([2,4,8])) # 16

"""
def good_solution(common):
    answer = 0
    a,b,c = common[:3]
    if (b-a) == (c-b):
        return common[-1]+(b-a)
    else:
        return common[-1] * (b//a)
    return answer
"""