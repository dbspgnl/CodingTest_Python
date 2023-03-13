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
# 그리디
n,k = map(int, input().split())
aList = [0]*n
for i in range(n):
    aList[i] = int(input())

count = 0
for i in reversed(range(n)):
    if aList[i] <= k:
        count += int(k/aList[i]) # 몫 넣기
        k = k % aList[i]
print(count)