"""
2차원에 배열에서 특정 수를 찾는 건데 배열의 크기가 10^5(10만)이므로 모든 수를 찾는 N^2는 불가능
따라서 절반씩 줄여가면서 찾는 이진탐색을 사용한다.
N의 정사각형에서 K번째 해당하는 값 구하기
2차 배열의 값은 A[i][j] = i*j
"""
N = int(input()) # 리스트의 크기
K = int(input()) # 구하고자 하는 인덱스
start = 1 # 좌
end = K # 우
ans = 0

# 이진탐색 수행
while start <= end:
    middle = int((start+end)/2)
    cnt = 0 # 중앙값보다 작은 수 계산
    for i in range(1, N+1): # 모든 값을 돌면서
        cnt += min(int(middle/i),N) # cnt에 중앙 인덱스를 i로 나눈 값과 N중 작은 값을 더함
    if cnt < K:
        start = middle+1 # 좌 +1
    else: # 최소값이랑 중앙값이 크거나 같아질 때까지
        ans = middle
        end = middle-1
print(ans)
"""
3
7
=6
"""