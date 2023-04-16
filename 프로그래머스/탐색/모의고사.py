def solution(answers):
    answer = [0]*4
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    maxc = 0
    for i in range(len(answers)):
        if(answers[i] == a[i%5]): answer[1] += 1
        if(answers[i] == b[i%8]): answer[2] += 1
        if(answers[i] == c[i%10]): answer[3] += 1
    maxc = max(answer)
    result = []
    for i in range(4):
        if answer[i] == maxc: result.append(i)
    return result

print(solution([1,2,3,4,5])) #[1]
print(solution([1,3,2,4,2])) #[1,2,3]
print(solution([1,1,1,1,1,1,1,1,1]))