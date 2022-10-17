"""
주어진 수에서 특정 조건 수를 찾을 때, 양쪽에서 포인트를
이동시키는 것처럼 조건을 찾아가는 방식이다.
따라서 시간복잡도는 O(nlogn)이다.
"""

# 대표 문제: 좋은 수 구하기

"""
1. 아이디어: 주어진 수 2개의 합이 주어진 수에 존재하면 그 수를 좋은 수라고 한다.
2. 시간복잡도: N^2에서 이중 포문을 사용하면 N^3가 되므로 투포인트를 사용한다.
3. 자료구조: 
N :데이터 개수
Result : 좋은 수 저장 
A(수 데이터 저장)
A 리스트 정렬
"""

"""
A[i] + A[j] > K: j--; # 두 합이 원하는 값보다 크면 우측 내림
A[i] + A[j] < K: i++; # 두 합이 원하는 값보다 작으면 좌측 올림
A[i] + A[j] == K: count++; 프로세스 종료
"""

import sys
input = sys.stdin.readline
N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()

# K는 목표값으로 1,2,3,4, ... 9, 10으로 올라간다.
for k in range(N): # 한 번씩 주어진 수를 체크한다 (좋은 수가 주어진 수에 포함되어 있기 때문)
    find = A[k] # 목표 값
    i = 0 # 좌측 포인터(index)
    j = N-1 # 우측 포인터(index)
    # 투포인터 알고리즘
    while i < j: # find는 서로 다른 두 수의 합을 체크
        if A[i]+A[j] == find: # 만약 합이 타겟이랑 같으면 찾은 거임
            if i!=k and j!=k: # 찾았는데 좌/우 인덱스가 타겟 인덱스 아니면
                Result +=1 # 종료
                break
            elif i == k: # 찾았는데 좌 포인터가 타겟 인덱스랑 같으면 한 칸 더 올리고 시작
                i +=1
            elif j == k: # 찾았는데 우 포인터가 타겟 인덱스랑 같으면 한 칸 더 내리고 시작
                j -=1
        elif A[i]+A[j] < find: # 만약 합이 타겟보다 작으면 좌측 올림
            i +=1
        else: # 만약 합이 타겟보다 크면 좌측 내림
            j -=1
print(Result)

"""
10 # 수의 개수
1 2 3 4 5 6 7 8 9 10
= 8
"""