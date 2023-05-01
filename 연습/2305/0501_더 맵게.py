"""
다음 규칙을 따른다.
가장 안매운 음식 +그 다음 안매운 음식*2
k = 7보다 모두 맵고,섞은 횟수는 2회
"""
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K: # 1번 + 2번*2을 다시 스코프에 넣다
        new = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, new)
        answer +=1
        if scoville[0] < K and len(scoville) == 1:
            return -1 # 마지막 하나가 남을 때까지도 목표치보다 낮으면
    return answer

print(solution([1, 2, 3, 9, 10, 12],7)) #2