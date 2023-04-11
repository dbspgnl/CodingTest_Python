import heapq
def solution(operations):
    # heap = []
    # i = 0
    # operation_list = []
    # number_list = []
    # for operation in operations:
    #     split = operation.split(" ")
    #     operation_list.append(split[0])
    #     number_list.append(split[1])
    # heapq.heapify(number_list)
    # while i < len(operations):
    #     if operation_list[i] == "I":
    #         heap.append(number_list[i])
    #     else: # D
    #         if number_list[i] == 1: # 최댓값
    #
    #             pass
    #         else: # 최솟값
    #             pass
    #         pass
    #     i += 1
    # print(operation_list)
    # print(number_list)
    # # while i < len(operations):
    # #     for oper in operations:
    #
    # # if heap: return [heapq.heappop(max())]
    heap = []
    for operation in operations:
        oper, number = operation.split()
        if oper == "I":
            heapq.heappush(heap, int(number))
        else:
            if len(heap) > 0:
                if number == "1":
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0]))
                else:
                    heapq.heappop(heap)
    # print(heapq.nlargest(1, heap)[0])
    # print(heap[0])
    if len(heap) == 0: return [0,0]
    else: return [heapq.nlargest(1, heap)[0], heap[0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333, -45]