# 인접 공식은 dp[i] = max(dp[i-1], dp[i-2]+k)
def solution(sticker):
    n = len(sticker)
    if n == 1: return sticker[0]
    # 맨 앞
    dp1 = [0 for _ in range(n)]
    dp1[0] = sticker[0]
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
    # 맨 앞x
    dp2 = [0 for _ in range(n)]
    dp2[0] = 0
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    return max(max(dp1), max(dp2))


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))  # 36
print(solution([1, 3, 2, 5, 4]))  # 8