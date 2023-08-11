import heapq
def solution(A, B):
    A = [-a for a in A]
    B = [-b for b in B]
    heapq.heapify(A)
    heapq.heapify(B)
    for _ in range(len(B)):
        a_max = heapq.heappop(A)
        b_max = heapq.heappop(B)
        print(a_max)
        print(b_max)
        if b_max < a_max: heapq.heappush(B, b_max) # 부등호 반대로
        else: heapq.heappop(A)

        # heapq.heappush(works, i)

    return len(A)

print(solution([5,1,3,7], [2,2,6,8])) #3
print(solution([2,2,2,2], [1,1,1,1])) #0