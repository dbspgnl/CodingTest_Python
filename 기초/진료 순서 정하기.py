# 높은 순으로 번호를 매김 1, 2, 3...
# 높은 순으로 정렬하고 번호 찾음
# 원래 배열에서 해당 값을 찾아서 몇 번째 인덱스인지 확인

def solution(emergency):
    answer = emergency.copy() # 원본 데이터를 그대로 사용하면 문제가 발생...
    order = sorted(answer)
    count = 0
    for i in order[::-1]:
        count += 1
        answer[emergency.index(i)] = count
    return answer

print(solution([3, 76, 24])) # [3, 1, 2]
print(solution([1, 2, 3, 4, 5, 6, 7])) # [7, 6, 5, 4, 3, 2, 1]
print(solution([30, 10, 23, 6, 100])) # [2, 4, 3, 5, 1]

"""
def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
"""