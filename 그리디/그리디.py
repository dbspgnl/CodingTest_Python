"""
현재 상태에서 지금 처리할 수행이 최선이라고 가정하고 처리하는 방법
= 실전에서는 생각하기 매우 어려움, 사용 이유와 반례 찾기 연습
ex) 거스름돈 구하기
큰 금액의 동전부터 차감 (동전의 배수 조건에 의해서)

1. 아이디어
- 동전을 저장한 뒤, 반대로 뒤집음
- 동전 for
    - 동전 사용 개수 추가
    - 동전 사용한 만큼 k값 갱신

2. 시간복잡도
- O(N)

3. 자료구조
- 동전 금액 : int[]
- 동전 사용 cnt : int
- 남은 금액 : int
"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # 동전의 종류, 원하는 합
coins = [int(input()) for _ in range(N)]
coins.reverse() # 큰 수부터 처리한다.
cnt = 0

for each_coin in coins:
    cnt += K // each_coin # 원하는 합을 동전으로 나눠서 횟수를 올린다 = 동전 몇 개 썼는지
    K = K % each_coin # 원하는 합을 동전으로 나누면 원하는 합이 변동된다.

print(cnt)

"""
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
=6
"""