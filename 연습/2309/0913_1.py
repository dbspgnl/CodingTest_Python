# 입국심사
def solution(n, times):
    answer = 0
    start = 1
    end = max(times)*n # 최대로 걸리는 시간
    while start < end:
        mid = (start+end)//2
        temp = 0
        for time in times:
            temp += mid//time
        if temp >= n: # 임시 답이 입국자에 해당하는가?
            end = mid
        else:
            start = mid+1
        answer = start
    return answer

# 입국자, [심사대 처리시간] # 최소 시간
print(solution(6,[7, 10]))	#28
print(solution(6,[7, 10, 15]))	#21