"""
처음 테스트 케이스 횟수 T가 주어진다.
이후 n과 m을 공백으로 받는다.
n*m의 행렬에서 m개 만큼 금맥정보를 받고, n번 반복해서 채운다.
맨 좌측에서 우측으로 한 열씩 이동할 때 마지막 열에서 최대 금맥의 합이 제일 큰 값은?
이때 이동은 우측-아래, 우측, 우측-위로 이동할 수 있다.
"""
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    dp = []
    index = 0
    for i in range(n): # 한 줄씩 담기
        dp.append(array[index:index + m])
        index += m
    for j in range(1, m): # 1열씩 이동
        for i in range(n):
            if i == 0: left_up =0 # 위쪽 범위 벗어남
            else: left_up = dp[i-1][j-1]
            if i == n-1: left_down = 0 # 아래쪽 범위 벗어남
            else: left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0 # 최고값
    for i in range(n):
        result = max(result, dp[i][m-1]) # 마지막 열에서 최고값
    print(result)
"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
= 19
16
"""