# def solution(numbers):
#     answer = []
#     index = 0
#     while numbers:
#         first = numbers.pop(0)
#         index +=1
#         for n in numbers: 
#             if n > first:
#                 answer.append(n)
#                 break         
#         if len(answer) != index:
#             answer.append(-1)   
#     return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer

print(solution([2, 3, 3, 5])) # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2]))	# [-1, 5, 6, 6, -1, -1]