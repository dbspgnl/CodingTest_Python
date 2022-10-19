"""
백트래킹: 모든 경우의 수를 확인할 때 사용한다. (ex: 3,2,1 / 3,1,2 / ... 1,2,3)
대표적으로 수열 문제가 있다.
시간복잡도는 중복일 때 N^N (최대 N=8) / 중복 불가일 때 N! (최대 N=10)
방문 여부 확인 배열 / 선택한 값 입력 배열

1. 아이디어
- 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문 여부 확인)
- 재귀함수에서 M개를 선택할 경우 print

2. 시간복잡도
- N! : n이 8까지 이므로 가능

3. 자료구조
- 결과값 저장 int[]
- 방문여부 체크 bool[]

"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rs = []
chk = [False] * (N+1)

def recur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            recur(num+1)
            chk[i] = False # 이렇게 하지 않으면 [1, 2, 3] 세 개가 된다.
            rs.pop() # 중복 허용하지 않으므로 마지막을 제거 해준다.

recur(0)

"""
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
"""