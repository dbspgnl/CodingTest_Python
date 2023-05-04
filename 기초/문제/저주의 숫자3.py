def solution(n):
    a = [i for i in range(1, 200) if i % 3 !=0 and "3" not in str(i)]
    return a[n-1]

print(solution(100))

"""
def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
"""