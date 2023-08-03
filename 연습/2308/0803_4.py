def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for i in range(0, n-1): # 행(줄)
        for j in range(len(triangle[i])): # 열(칸)
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j]) # 다음줄 첫번째
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1]) # 다음줄 두번째
    return max(dp[-1]) # 마지막 줄에서 최대값

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30