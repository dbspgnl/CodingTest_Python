# 입국심사
def solution(n, times):
    answer = 0
    start = 1
    end = max(times)*n
    while start < end:
        mid = (start+end)//2 # 걸리는 시간
        temp = 0
        for time in times:
            temp += mid//time
        if temp >= n: # 딱 떨어지는 경우가 있다.
            end = mid
        else:
            start = mid+1
        answer = start
    return answer

print(solution(6, [7,10])) # 28
print(solution(6,[7,10,15])) # 21

