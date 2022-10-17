"""
어떠한 배열을 체크할 때, 그 체크를 배열로 하는 방식이다.
그 체크할 배열을 슬라이딩 윈도우라고 해서 범위가 있고,
빼고 넣고 하면서 처리하는데 마치 캐시를 담고 있는 느낌이다.

"""

# 대표 문제: 최솟값 찾기

"""
해석: 
N = 10
A = 1,2,3,4,5,6,7,8,9,10
L = ?  A(3-3+1)~A(3) / A(10-3+1=8)~A(10) ~ L은 윈도우 범위 = 3
D = 최솟값 (윈도우에서 최솟값)
"""

# 슬라이딩 윈도우의 핵심은 윈도우 배열에 값을 하나씩 빼고 넣고 하면서 체크하는 것
# : 값이 들어올 때는 들어온 값이 이미 있는 값보다 작을 경우 이미 있는 값들을 지워버린다.
# : 범위 안에서 벗어나는 앞에 값은 지워준다. (윈도우가 한 칸씩 이동한다)


from collections import deque
N, L = map(int, input().split()) # 전체 수 / 윈도우 크기
print()
print(N)
print(L)
mydeque = deque()
now = list(map(int, input().split())) # 실제 값이 담긴 배열

for i in range(N): # N번 실행
    # 나보다 큰 데이터 삭제
    print(mydeque)
    while mydeque and mydeque[-1][0] > now[i]: # 내 덱에 마지막 값이 들어온 값보다 크면 빼준다. 덱 배열만큼
        mydeque.pop() # 뒤에서 제거
    mydeque.append((now[i], i)) # 값과 인덱스를 넣는다.
    if mydeque[0][1] <= i-L: # 제일 앞에 값이 윈도우 범위를 벗어나면
        mydeque.popleft() # 앞에서 제거
    print(mydeque[0][0], end=' ')






"""
12 3 # 숫자의 개수, 슬라이딩 윈도우 크기
1 5 2 3 6 2 3 7 3 5 2 6
= 1 1 1 2 2 2 2 2 3 3 2 2
"""