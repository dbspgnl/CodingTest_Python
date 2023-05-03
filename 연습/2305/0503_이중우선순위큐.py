# I 숫자	큐에 주어진 숫자를 삽입합니다.
# D 1	큐에서 최댓값을 삭제합니다.
# D -1	큐에서 최솟값을 삭제합니다.
# 큐가 비어있다면 [0,0]을 반환한다.
# 큐가 있다면 [최댓값, 최솟값]을 반환한다.
import heapq
def solution(operations):
    heap = []
    for operation in operations:
        oper, number = operation.split()
        if oper == "I": # 추가
            heapq.heappush(heap, int(number))
        else:
            if len(heap) >0:
                if number == "1":
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0])) # 가장 큰 값 제거
                else:
                    heapq.heappop(heap)
    if len(heap) == 0: return [0,0]
    else: return [heapq.nlargest(1,heap)[0], heap[0]] # 최댓값, 최솟값

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))  # [333, -45]