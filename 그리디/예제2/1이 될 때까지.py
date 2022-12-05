"""
자연수 n과 k이 주어진다.
n을 k으로 나눌 수 있으면 나누고, 나눌 수 없으면 -1을 한다.
이 몫이 1이 될 때까지 과정 횟수는 몇 번인가?
"""
n, k = map(int, input().split())
result = 0
while True:
    target = (n//k) * k # k로 한 번에 나눠질 때까지 빼기
    result += (n-target)
    n = target
    if n < k:
        break
    result += 1
    n //= k # 몫 남기기
result += (n-1)
print(result)
"""
25 5
=2
"""