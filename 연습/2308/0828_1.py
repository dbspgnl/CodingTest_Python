# 건널 수 있는 징검다리 번호 배열과 한 번에 건널 수 있는 거리 k가 주어진다.
# 건널 수 있는 사람 수?
def solution(stones, k):
    answer = 0
    left, right = 1, max(stones)
    while left <= right:
        cnt = 0
        mid = (left+right)//2
        # 카운팅
        for stone in stones:
            if (stone-mid) <= 0: # 타겟이 0보다 작으면 건널 수 있다.
                cnt +=1
            else: # 그렇지 않으면 다시 구한다.
                cnt = 0
            if cnt >= k: break # 만약, 다시 구하는 로직에서 목표치를 넘으면 통과
        # 정답 찾기
        if cnt < k: # 목표치 보다 작으면
            left = mid + 1
        else:
            answer = mid
            right = mid -1
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) #3