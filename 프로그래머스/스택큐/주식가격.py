# 해당 시점에서 가격이 떨어질 때까지의 시간을 담는 배열
from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        print("i: ",i)
        print(stack)
        while stack and stack[-1][1] > prices[i]:
            print("stack[-1][1]: ",stack[-1][1])
            past_idx, _ = stack.pop()
            print("past_idx, _:", past_idx, _)
            answer[past_idx] = i - past_idx
            print(answer[past_idx])
        stack.append([i, prices[i]])
    for i, _ in stack:
        answer[i] = len(prices) - i - 1
    return answer
# print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
print(solution([1, 2, 3, 0, 2, 3, 3, 4, 1])) #[3, 2, 1, 5, 4, 3, 2, 1, 0]
