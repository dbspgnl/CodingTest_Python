"""
다양한 종류의 동전을 최소한 사용해서 해당 가격에 맞는 동전 수를 구하는 문제는
대표적인 그리드 문제이다.
N = 동전 개수
K = 목표 금액 (남은 금액)
A = 동전 데이터 리스트
* 가치가 큰 동전부터 선택해야 개수를 최소로 구성할 수 있음
"""
N,K = map(int, input().split())
A = [0]*N
for i in range(N): # 동전 종류 담기
    A[i] = int(input())
count = 0 # 동전 사용 개수
for i in range(N-1, -1, -1): # 배열이므로 N-1부터, 끝까지, -1씩 감소
    if A[i] <= K: # 현재 동전의 가치가 K(목표 금액, 남은 금액)보다 작으면
        count += int(K/A[i]) # ex) 4200/1000 = 4(동전 4개 담기)
        K = K%A[i] # 해당 금액 사용한 나머지를 갱신
print(count)
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