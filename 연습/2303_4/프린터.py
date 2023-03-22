# 우선순위 출력 설정이 된 프린터에서 내 프린트물은 몇 번째에서 출력될까?
def solution(priorities, location):
    # 1. Queue 를 만든다.
    printer = [(i,p) for i,p in enumerate(priorities)] # 배열을 튜플로 만드는 방법
    turn = 0
    while printer:
        job = printer.pop(0) # 앞에 하나 꺼냄
        if any(job[1] < other_job[1] for other_job in printer): # 지금 값이 다른 것들의 값보다 작으면
            printer.append(job) # 뒤로 보냄 (우선 순위 뒤로)
        else:
            turn += 1 # 지금 값보다 작은 게 없으면 = 가장 크면 = 출력 처리
            if job[0] == location: # 내가 원하는 순서랑 같으면 내꺼임으로 종료
                break
    return turn

print(solution([2,1,3,2],0))