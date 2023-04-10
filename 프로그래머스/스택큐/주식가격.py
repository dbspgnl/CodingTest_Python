# 해당 시점에서 가격이 떨어질 때까지의 시간을 담는 배열
from collections import deque
def solution(prices):
    length = len(prices)
    answer = [ i for i in range(length-1,-1,-1)]
    print(answer)
    stack = [0] # 인덱스(시간)
    for i in range(1, length):
        print("i: ",i)
        print("stack: ",stack)
        while stack and prices[stack[-1]] > prices[i]: # 이전 prices가 현재 prices보다 크면
            print("stack[-1] = pop() = j: ",stack[-1]) # 마지막 스택
            # print("pop: ", j)
            print("prices[stack[-1]]: ", prices[stack[-1]]) # 마지막 스택(시간대)의 값
            j = stack.pop()
            print("i-j: ", i-j) # 현재 시간에서 이전 시간까지를 빼줌
            answer[j] = i-j
            print("ans: ", answer)
        stack.append(i)
    return answer

# print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
# 1이 3까지 증가하다가떨어지는 시간은 4초이다. (없다)
print(solution([1, 2, 3, 0, 2, 3, 3, 4, 1])) #[3, 2, 1, 5, 4, 3, 2, 1, 0]
