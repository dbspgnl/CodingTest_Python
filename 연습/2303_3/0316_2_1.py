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
# 그리드: 최선의 해를 가정하면서 반복하는 알고리즘
n,k = map(int, input().split())
cList = [0]*n

# 동전 입력 받기
for i in range(n):
    cList[i] = int(input())

count = 0
for i in range(n-1, -1, -1): #9~0
    coin = cList[i]
    if coin <= k:
        count += int(k/coin)
        k = k%coin
print(count)