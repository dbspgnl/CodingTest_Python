"""
N의 범위가 100,000이며 큰 범위에서 특정 수를 찾아야 하므로 이진탐색을 이용한다.
데이터 개수가 주어지고, 찾아야 할 수가 주어진다.
"""
N = int(input()) # 주어진 수
A = list(map(int, input().split()))
A.sort()
M = int(input()) # 찾을 수 개수
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i] # 추적할 값 하나씩 꺼내서 처리
    # 이진 탐색 시작
    start = 0
    end = len(A)-1
    while start <= end:
        midi = int((start+end)/2) # 중앙값 인덱스
        midv = A[midi] # 중앙값
        if midv > target: # 타겟이 작으면
            end = midi-1 # 작은 값으로
        elif midv < target: # 타겟이 더 크면
            start = midi+1 # 큰 값으로
        else:
            find = True # 찾으면 종료
            break
    if find:
        print(1)
    else:
        print(0)

"""
5
4 1 5 2 3
5
1 3 7 9 5
=1
1
0
0
1
"""