"""
다음 규칙을 따른다.
가장 안매운 음식 +그 다음 안매운 음식*2
1 + (2*2) = 5
[5,3,9,10,12]
3 + (5*2) = 13
[13,9,10,12]
k = 7보다 모두 맵고,섞은 횟수는 2회
"""
import heapq
def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville) # 정렬 자동
    while scoville[0] < k:
        new = heapq.heappop(scoville) + (heapq.heappop(scoville)*2) # 문제 공식
        heapq.heappush(scoville, new)
        answer +=1
        if scoville[0] < k and len(scoville) ==1:
            return -1
    return answer

print(solution([1, 2, 3, 9, 10, 12],7)) #2