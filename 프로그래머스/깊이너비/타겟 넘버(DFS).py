# def dfs(numbers, target, index, value): # 타겟은 고정
#     global count
#     count = 0
#     if index == len(numbers) & value == target: # 모두 탐색 후, 변경된 value가 타겟이면
#         count +=1
#         return
#     elif index == len(numbers): # 끝까지 탐색 완료 시 종료
#         return
#     dfs(numbers, target, index+1, value + numbers[index]) # 양수를 모두 탐색한다.
#     dfs(numbers, target, index+1, value - numbers[index]) # 음수를 모두 탐색한다.
#
# def solution(numbers, target):
#     global count
#     dfs(numbers, target, 0, 0)
#     return count
#
# print(solution([1, 1, 1, 1, 1], 3)) #5
# print(solution([4, 1, 2, 1], 4)) #2

def solution2(numbers, target):
    answer = 0
    stack = [[numbers[0],0], [-1*numbers[0],0]] # 초기화
    n = len(numbers)
    while stack:
        temp, index = stack.pop()
        index +=1
        if index < n:
            stack.append([temp+numbers[index],index])
            stack.append([temp-numbers[index],index])
        else:
            if temp == target:
                answer +=1
    return answer

print(solution2([1, 1, 1, 1, 1], 3)) #5
print(solution2([4, 1, 2, 1], 4)) #2