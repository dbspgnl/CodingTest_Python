# 요청 시점과 작업 시간이 주어진 배열을 담은 배열이 주어진다.
# 작업을 하나씩 하는 상황에서 모든 작업을 처리하는데 '평균' 최소 시간 구하기.
# 투포인트
import heapq
def solution(jobs):
    cnt,now,i,start = 0,0,0,-1 # 시간,현재(끝),작업수,시작
    heap = []
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now: # 해당 요청시간이 범위 안
                heapq.heappush(heap, [job[1],job[0]])
        if len(heap) > 0: # 힙이 있으면
            current = heapq.heappop(heap)
            start = now
            now += current[0] # 현재+작업시간 = 끝나는 시점
            cnt += (now - current[1]) # 작업 시간만 카운팅 누적
            i +=1
        else:
            now +=1
    return int(cnt/len(jobs)) # 누적시간의 평균
print(solution([[0, 3], [1, 9], [2, 6]])) #9
print(solution([[1,4],[7,9],[20,3]])) #5