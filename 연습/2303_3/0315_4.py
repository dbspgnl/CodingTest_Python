"""
# 동전 종류 수 / 돈
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
= 6
# 동전 종류 수 만큼 종류를 나열함
# 사용한 동전 개수
"""
# 그리디: 최적의 해를 가정하면서 반복한다.
n,k = map(int, input().split())
cList = [0]*n

for i in range(n):
    cList[i] = int(input())

count = 0
for i in range(n-1, -1, -1): # 9부터 0까지
    coin = cList[i]
    if coin <= k:
        count += int(k/coin)
        k = k % coin
print(count)