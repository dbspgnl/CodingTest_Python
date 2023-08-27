import heapq
def solution(A, B):
    answer = []
    A = [-a for a in A]
    B = [-b for b in B]
    heapq.heapify(A)
    heapq.heapify(B)
    for _ in range(len(B)):
        a_max = heapq.heappop(A)
        b_max = heapq.heappop(B)
        if b_max < a_max: #이기면
            answer.append(b_max) # AB버리고, 결과만 담는다.
        else:
            heapq.heappush(B, b_max) # 지면 재활용한다.
    return len(answer)

print(solution([5,1,3,7], [2,2,6,8])) #3
print(solution([2,2,2,2], [1,1,1,1])) #0