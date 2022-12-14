"""
LIS(최장 증가 부분 수열)문제
처음 병사의 수 n이 정해진다.
각 병사의 전투력 정보가 정해진다.
병사의 전투력이 높은 순으로 해서 가장 긴 길이를 구할 때
순차적으로 진열하기 하기 위해서 병사를 제외한다면 몇 명을 빼야 하는가?
= 최소한으로 병사를 제외해서 가장 긴 길이를 가진 내림차순 구하기
- LIS의 핵심은 dp 테이블을 dp[i] = max(dp[i], dp[j]+1) 공식으로 구하는 것이다.
- j는 i보다 작은 이전 값이고, i는 현재 j는 i보다 앞의 값들을 순회하는 값이다.
"""
n = int(input())
array = list(map(int, input().split()))
array.reverse() # LIS(오름차순)처리를 위해
dp = [1]*n # dp 테이블
for i in range(1, n):
    for j in range(0, i): # 현재값i보다 앞의값j를 i까지 순회
        if array[j] < array[i]: # i보다 낮은 j이어야만 오름차순 처리 가능
            dp[i] = max(dp[i], dp[j]+1) # dp를 누적한다.
print(n - max(dp)) # 총 병사 수 - 최장 부분 수열 = 제외한 병사 수
"""
7
15 11 4 8 5 2 4
= 2
7
4 2 5 8 4 11 15
=5
"""