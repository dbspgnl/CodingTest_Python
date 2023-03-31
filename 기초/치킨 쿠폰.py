def solution(chicken):
    answer = 0
    while chicken >= 10 : # 10으로 나누는데 더 그보다 작을 때까지
        qu = chicken//10
        remain = chicken % 10
        chicken = qu + remain
        answer += qu
    return answer

print(solution(100))
print(solution(1081)) # 120 (서비스로 받은 치킨)

"""
# 수학적 접근: 10%를 계속 적용한다.
def solution(chicken):
    return int(chicken*0.11111111111)
"""