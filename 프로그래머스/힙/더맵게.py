"""
다음 규칙을 따른다.
가장 안매운 음식 + 그 다음 안매운 음식*2
1 + (2*2) = 5
[5,3,9,10,12]
3 + (5*2) = 13
[13,9,10,12]
k = 7보다 모두 맵고, 섞은 횟수는 2회
# 주어진 제한사항 조건이 엄청 큰 수임으로 무조건 힙을 사용해야한다.
# 힙: 특정한 규칙을 가진 트리로, 최댓값과 최솟값을 찾는 매우 빠른 완전이진트리.
"""
# 힙의 최소값은 heap[0]이다. 그 다음값은 [1]이 아니다. 반드시 pop하고 [0]으로 불러온다.
# 최대값은 역순으로 만들어서 사용한다.
# for num in nums:
#   heappush(heap, (-num, num))
import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) 
    while scoville[0] < K: # heap[0]은 최솟값이다
        new = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, new)
        answer +=1
        if scoville[0]<K and len(scoville) ==1:
            return -1 # 모든 음식을 k이상으로 만들 수 없으면 -1
    return answer

print(solution([1, 2, 3, 9, 10, 12],7)) #2