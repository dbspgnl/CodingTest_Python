# 이진탐색 (중간값을 계속 찾아가는 방식 )으로 처리
# 입국자 n명이 심사대 배열을 이용해서 통과한다. (심사대 최대 활용)
# 만약, 심사대가 비어있더라도 더 빨리 끝날 다른 심사대가 있다면 거길 이용한다.
# 최소로 끝날 심사 시간 구하기

def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n # 최대 예상시간
    while left < right:
        mid = (left + right) // 2
        total = 0 # 횟수마다 초기화하면서 누적값 계산
        for t in times:
            total += mid // t
        if total >= n: #
            right = mid
        else:
            left = mid + 1
    answer = left
    return answer

print(solution(6,[7, 10]))	#28
print(solution(6,[7, 10, 15]))	#21

'''
1. 최대 예상치 6*10 = 60이며 중앙값은 30 (혹은 33이라도 괜찮다)
2. 30은 타겟이 되고 배열의 값으로 나눈 몫을 누적합 = 최대 작업 횟수
    - (30 // 7 = 4) + (30 // 10 = 3) 따라서 7이고 이는 6보다 크다.
3. 타겟(mid)시간 내 심사 가능한 사람이 7명이라는 말은 그 시간보다 짧게 처리할 시간이 있다는 말
4. mid 뒷부분 없애고, 다시 mid를 구하면 15가 된다.
5. 다시 같은 방법으로 나눈다.
    - (15 // 7 = 2) + (15 // 10 = 1) 따라서 3이고 이는 6보다 작다.
6. 타겟(mid)시간 내 심사 가능한 사람이 3명은 6보다 작기 때문에 더 시간이 길어야 한다.
7. mid 앞부분을 없애고, 다시 mid를 구한다.  (15+30)//2 = 22
8. (22 // 7 = 3) + (22 // 10 = 2) 5<6(n) 더 커야 한다. left =22 right=30 mid=26
9. (26 // 7 = 3) + (26 // 10 = 2) 5<6(n) 더 커야 한다. left =26 right=30 mid=28
10. (28 // 7 = 4) + (28 // 10 = 2) 6=6 따라서 28이 정답
'''
