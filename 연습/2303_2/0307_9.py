# 백준 11047
# 그리디
n,k = map(int, input().split())
a = [0]*n
for i in range(n):
    a[i] = int(input())
count = 0
for i in range(n-1, -1, -1):
    if a[i] <= k: # 현재 동전의 가치가 k보다 적거나 같으면 구성에 추가
        count += int(k/a[i])
        k = k % a[i] # K를 현재 동전을 사용하고 남은 금액으로 갱신
print(count)
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