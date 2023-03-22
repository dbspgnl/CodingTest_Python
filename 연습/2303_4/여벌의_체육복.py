# n명의 학생들에 체육복을 잃어버린 학생 목록과 여벌이 있는 학생 목록을 비교하여 체육 수업을 들을 수 있는 학생의 수 구하기
def solution(n, lost, reserve):
    # 1. set을 만든다.
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    # 2. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려줌
    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
    # 3. 전체 학생 수에 lost_only에 남은 학생 수를 빼주면 = 체육복 있는 학생 수
    return n - len(lost_only)
print(solution(5,[2,4],[1,3,5]))

def solution2(n, lost, reserve):
    # 1. student 배열 생성
    student = [0] * (n+2)
    # 2. reserve/lost 정보 반영
    for r in reserve:
        student[r] +=1
    for l in lost:
        student[l] -=1
    # 3. 여분을 기준으로 앞뒤를 확인하여 체육복을 빌려준다.
    for i in range(1, n+1):
        if student[i] > 0:
            front = i-1
            back = i+1
            if student[front] < 0: # 체육복이 없으면
                student[i] -= 1 # 여벌을 넘겨줌
                student[front] += 1 # 여벌을 받음
            elif student[back] < 0:
                student[i] -= 1
                student[back] +=1
    # 4. 체육복을 갖고 있는 학생 수를 계산한다.
    answer = 0
    for i in range(1, n+1):
        if student[i] >= 0:
            answer +=1
    return answer
print(solution2(5, [2, 4], [1, 3, 5]))
