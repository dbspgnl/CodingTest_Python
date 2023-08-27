def solution(sticker):
    n = len(sticker)
    if n == 1: return sticker[0]
    # pick first
    dp1 = [0 for _ in range(n)]
    dp1[0] = sticker[0]
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])

    # pick second
    dp2 = [0 for _ in range(n)]
    dp2[0] = 0 # not pick
    dp2[1] = sticker[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    return max(max(dp1), max(dp2))


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))  # 36
print(solution([1, 3, 2, 5, 4]))  # 8