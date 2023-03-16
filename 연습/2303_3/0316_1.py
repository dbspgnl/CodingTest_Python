# 백트래킹: 모든 경우의 수를 확인한다. 순열 문제가 있다.
n,m = map(int, input().split())
chk = [False] * (n+1)
rs = []

def recur(num):
    if num == m:
        print(rs)
        return
    for i in range(1, n+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()
recur(0)