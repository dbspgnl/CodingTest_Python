# 그리디
n,k = map(int, input().split())
clist = [0] * n
for i in range(n):
    clist[i] = int(input())
count = 0
for i in range(n-1, -1, -1): # 역순
    coin = clist[i]
    if coin <= k:
        count += int(k/coin)
        k = k % coin
print(count)