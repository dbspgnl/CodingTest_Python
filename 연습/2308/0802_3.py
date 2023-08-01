# 백트래킹
import sys
input = sys.stdin.readline()
n,m = map(int, input.split())
rs = []
chks = [False] * (n+1)
def recur(num):
    if num == m:
        print(" ".join(map(str, rs)))
        return
    for i in range(1, n+1):
        if chks[i] == False:
            chks[i] = True
            rs.append(i)
            recur(num+1)
            chks[i] = False
            rs.pop()
recur(0)
