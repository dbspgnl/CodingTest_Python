# 첫번째 배열은 작업의 진행도와 순서
# 두번째 배열은 각 작업의 처리속도 (완료는 100)
# 결과: 각 배포할 때마다 몇개씩 배포하는가?
def solution(progresses, speeds):
    work_list = []
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        for day in range(1, 101):
            if p+(s*day) >= 100:
                work_list.append(day)
                break
    print(work_list) # [7, 3, 9]
    result = []
    for w in work_list:
        print(w)

    return "---"

print(solution([93, 30, 55],[1, 30, 5])) # [2, 1]
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])) # [1, 3, 2]