# 삼각형 형태로 배열이 주어 진다.
# 위에서 부터 아래로 내려오면서 누적할 때 가장 큰 값

def solution(triangle):
    n = len(triangle)
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = triangle[0][0] # 첫번째 값
    for i in range(0, n-1): # 한 줄씩
        for j in range(len(triangle[i])): # 한 칸씩
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])
    return max(dp[-1]) # 마지막 배열 원소 중 max값

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30

'''
이차원 배열로 하면 아래와 같다. 
7, 0, 0, 0, 0
3, 8, 0, 0, 0
8, 1, 0, 0, 0
2, 7, 4, 4, 0
4, 5, 2, 6, 5
다음줄의 값을 구해나가는 방식인데, 최대값만 구하면 되기 때문에
이미 존재하는 값과 더할 때 값 중 max로 비교해서 높은 값만 남겨둔다.
따라서 최종 마지막줄이 후보군 배열이 되고, 그 중 가장 높은 값을 취한다.
'''

# 참고
# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])