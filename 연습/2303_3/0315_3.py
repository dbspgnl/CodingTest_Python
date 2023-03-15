"""
#4P2 팩토리얼을 구하는 N,M을 입력받음
4 2
= 1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
#모든 경우의 수를 처리
"""
# 백트래킹: 모든 경우의 수를 찾을 때 사용한다. 대표적으로 순열 문제가 있다.
import sys
input = sys.stdin.readline

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
            rs.append(i) # 결과 담기
            recur(num+1) # 재귀 탐색
            chk[i] = False
            rs.pop()
recur(0)


