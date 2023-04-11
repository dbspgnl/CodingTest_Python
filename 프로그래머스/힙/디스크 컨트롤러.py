import heapq
def solution(jobs):
    answer,now,i = 0,0,0 # now: 현재시점
    start = -1 # job인덱스 0도 포함시키기 위해
    heap = [] # 끝나는 시간 / 시작시간 (역순저장)
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now: # 작업 가능
                heapq.heappush(heap, [job[1],job[0]]) # end / start
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now # 다음 작업을 위해 시작점을 초기화
            now += current[0] # 현재 작업의 끝나는 지점
            answer += (now - current[1]) # 현재 작업의 작업 시간
            i +=1
        else:
            now += 1
        print("---")
        print("i: ", i)
        print("start: ", start)
        print("now: ", now)
        print("job[0]: ", job[0])
        print("job[1]: ", job[1])
    return int(answer/len(jobs))
# now는 현재 시점이므로 시작점이 1000이면 1000번 찍어봐야 한다...
# print(solution([[0, 3], [1, 9], [2, 6]])) #9
print(solution([[1,4],[7,9],[20,3]])) #5
