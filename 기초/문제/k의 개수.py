def solution(i, j, k):
    answer = 0
    for n in range(i, j+1):
        for w in list(str(n)):
            if str(k) == str(w):
                answer += 1
    return answer

print(solution(1,13,1)) #6
print(solution(10,50,5)) #5
print(solution(3,10,2)) #0

"""
# 카운터 함수 사용
def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer
"""
