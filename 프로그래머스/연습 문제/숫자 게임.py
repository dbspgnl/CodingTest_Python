import heapq
def solution(A, B):
    A = [-a for a in A]
    B = [-b for b in B]
    heapq.heapify(A)
    heapq.heapify(B)
    answer = []
    for _ in range(len(B)):
        a_max = heapq.heappop(A)
        b_max = heapq.heappop(B)
        if b_max < a_max:
            answer.append(b_max)
        else:
            heapq.heappush(B, b_max)
    return len(answer)

print(solution([5,1,3,7], [2,2,6,8])) #3
print(solution([2,2,2,2], [1,1,1,1])) #0
