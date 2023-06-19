# 학생 수와 체육복을 잃어버린 학생 번호 배열, 여분을 가진 학생 번호 배열이 주어진다.
# 최대 몇 명이 체육복을 입을 수 있는가?
def solution(n, lost, reserve):
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    for r in reserve_only:
        front = r-1
        back = r+1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
    return n - len(lost_only)

print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(3, [3], [1]))  # 2