"""
정렬된 값에서 특정 값을 반으로 나눠가면서 찾는 방법
M개의 수 이진탐색 : O(M*lgN)
입력 개수가 10^5정도의 경우라면 의심해본다.

1. 아이디어
- N개의 숫자를 정려
- M개를 for 돌면서, 이진탐색
- 이진탐색 안에서 마지막에 데이터 찾음녀, 1출력, 아니면 0출력

2. 시간복잡도
- N개의 입력값 정렬 = O(NlgN)
- M개를 N개 중에서 탐색 = O(M * lgN)
- 총합 : O((N+M)lgN) 가능

3. 자료구조
- N개의 숫자 : int[]
- M개의 숫자 : int[]
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

nums.sort() # 이진탐색 가능

def search(st, en, target):
    if st == en:
        if nums[st] == target:
            print(1)
        else:
            print(0)
        return
    mid = (st+en)//2
    if nums[mid] < target:
        search(mid +1, en, target)
    else:
        search(st, mid, target)

for each_target in target_list:
    search(0, N-1, each_target)

"""
5
4 1 5 2 3
5
1 3 7 9 5
= 1
1
0
0
1
"""