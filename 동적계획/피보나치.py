"""
피보나치는 대표적인 DP문제이다.
메모리제이션 방식의 탑다운 방식과
반복문을 사용한 보텀업 방신이 있다.
"""
# 탑다운
d = [0]*100
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]
print(fibo(99)) # 218922995834555169026

#보텀업
d2 = [0]*100
d2[1] = 1
d2[2] = 1
n = 99
for i in range(3, n+1):
    d2[i] = d2[i-1]+d2[i-2]
print(d2[n]) # 218922995834555169026