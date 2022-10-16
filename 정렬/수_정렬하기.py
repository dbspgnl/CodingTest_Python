"""
파이썬에서 sort()함수를 정렬할 수 있다.
이중 for문을 이용한 방식은 O(n^2)으로 N이 매우 작아야 할 수 있다.
"""

N = int(input()) # 수의 개수
A = [0]*N

for i in range(N):
    A[i] = int(input()) # 값 입력 받음

for i in range(N-1): # 루프 횟수 (N-1번 한다)
    for j in range(N-1-i): # 2개씩 비교해서 (N-1)-i번 한다.
        if A[j] > A[j+1]: # 앞에가 더 크면 변경
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp

for i in range(N):
    print(A[i])


"""
5 # 수의 개수 
5
2
3
4
1
= 1
= 2
= 3
= 4
= 5

"""