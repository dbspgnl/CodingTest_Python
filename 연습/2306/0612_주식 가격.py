# 각 주식의 가격이 배열로 주어졌을 때, 각 배열이 떨어지는 시점을 구하는 배열
from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]:
            past_idx, _ = stack.pop()
            answer[past_idx] = i - past_idx
        stack.append([i, prices[i]])
    for i, _ in stack:
        answer[i] = len(prices) - i - 1
    return answer

# print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
print(solution([1, 2, 3, 0, 2, 3, 3, 4, 1]))  # [3, 2, 1, 5, 4, 3, 2, 1, 0]