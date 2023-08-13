# 거리가 n, 현재 설치된 기지국 배열, 전파 범위 w가 주어진다.
# 최소의 기지국을 추가하여 모든 거리에 전파를 적용하자.
from math import ceil
def solution(n, stations, w):
    answer = 0
    W = (w*2)+1 # 전파 전체 범위
    start =1
    for s in stations:
        answer += max(ceil((s-w-start)/W), 0)
        start = s + w + 1
    if n >= start:
        answer += ceil((n - start + 1)/W)
    return answer

print(solution(11, [4, 11],	1)) # 3
print(solution(16, [9], 2)) # 3