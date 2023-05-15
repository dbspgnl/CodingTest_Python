# 주어진 배열을 더 하거나 빼거나 해서 원하는 target 구하는 방법의 수
def solution(numbers, target):
    answer = [0]
    count = 0
    for num in numbers:
        temp = [] # Queue
        for ans in answer:
            temp.append(ans + num)
            temp.append(ans - num)
        answer = temp
    for ans in answer:
        if ans == target:
            count +=1
    return count

print(solution([1, 1, 1, 1, 1], 3)) #5
print(solution([4, 1, 2, 1], 4)) #2