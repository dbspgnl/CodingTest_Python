# 요청 시점과 작업 시간이 주어진 배열을 담은 배열이 주어진다.
# 작업을 하나씩 하는 상황에서 모든 작업을 처리하는데 '평균' 최소 시간 구하기.
# 투포인트
import heapq
def solution(jobs):
    cnt, now, i, start = 0,0,0,-1
    heap = []
    while i < len(jobs):
        for job in jobs: # 작업 담기
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now # 시점 변경
            now += current[0] # 현재+작업시간 = 끝나는 시점
            cnt += (now - current[1]) # 현재-요청시점 = 빈 시간 없이 작업시간만 누적
            i +=1
        else:
            now+=1 # 시간
    return int(cnt/len(jobs)) # 순수 작업 시간을 작업 수로 나눔 = 평균 작업 시간

print(solution([[0, 3], [1, 9], [2, 6]])) #9
print(solution([[1,4],[7,9],[20,3]])) #5