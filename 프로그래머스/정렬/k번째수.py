def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        i, j, k = map(int, commands[index])
        new = array[i-1:j]
        new.sort()
        print(new)
        answer.append(new[k-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])) # [5,6,3]