#Top-Down
# import sys
# input = sys.stdin.readline
N = int(input())
D = [-1]*(N+1) # DP테이블 세팅
D[0] = 0 # 첫번째 값 0
D[1] = 1 # 두번째 값 1

def fibo(n):
    if D[n] != -1: # 계산했던 부분은 스킵
        return D[n]
    D[n] = fibo(n-2) + fibo(n-1)
    return D[n]

fibo(N)
print(D[N])
# 6 = 8

#----------------
# Bottom-Up 좀 더 안전
K = int(input())
D = [-1]*(K+1)
D[0]=0
D[1]=1
for i in range(2, N+1):
    D[i]=D[i-1]+D[i-2]
print(D[N])