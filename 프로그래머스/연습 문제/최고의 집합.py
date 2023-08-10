# !자연수 집합 요소의 개수 n과 목표 s가 주어 진다.
# n개의 값을 사용한 합이 s인 배열을 만들고, 그 중 곱이 가장 큰 값을 구하기.
# n=2 s=8 {1,7},{2,6},{3,5},{4,5} = [4,5]
from collections import defaultdict
def solution(n, s):
    answer = []
    if n > s: return[-1]
    div = s//n
    mod = s%n
    for _ in range(n-mod): # 총 갯수 - 나머지
        answer.append(div)
    for _ in range(mod):
        answer.append(div+1)
    return answer

print(solution(2,9)) #[4, 5]
print(solution(2,1)) #[-1]
print(solution(2,8)) #[4, 4]
print(solution(3,8)) #[2,3,3]