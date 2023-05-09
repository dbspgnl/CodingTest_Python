# 학생 수와 체육복을 잃어버린 학생 번호 배열, 여분을 가진 학생 번호 배열이 주어진다.
# 최대 몇 명이 체육복을 입을 수 있는가?
def solution(n, lost, reserve):
    reverse_only = set(reserve) - set(lost) # 잃지 않고 여분있는 학생
    lost_only = set(lost) - set(reserve) # 잃어버리기만 한 학생
    for r in reverse_only: # 여분
        front = r-1 # 앞에 학생
        back = r+1 # 뒤에 학생
        if front in lost_only: # 앞 학생이 잃어버리기만 한 학생이면
            lost_only.remove(front) # 그 학생한테 주고 잃어버린 명단에서 제외
        elif back in lost_only: # 뒤 학생도 같은 방법으로
            lost_only.remove(back)
    return n - len(lost_only) # 전체 학생 수에서 오직 잃어버린 학생 뺌 = 체육복 있는 학생

print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(3, [3], [1]))  # 2