"""
백준: 1931
회의 시간이 정해진 임의의 회의가 주어지고, 첫 회의부터 마지막 끝나는 시간 안에
최대로 회의를 몇 개까지 넣을 수 있는가?
겹치지 않게 회의를 넣어야 한다. 종료 시간이 빠른 순서대로 정렬해서 배치한다.
만약 종료시간이 같은 회의가 여러 개면 시작 시간이 빠른 순으로 정렬한다.
N = 회의 개수
A = 회의 정보 저장
A 리스트 정렬
"""
N = int(input())
A = [[0]*2 for _ in range(N)] # [종료시간][시작시간] 배열

for i in range(N): # 회의 시간 담기
    S, E = map(int, input().split())
    A[i][0] = E # 종료 시각 우선 정렬을 위해 앞에다 넣음
    A[i][1] = S
A.sort() # 종료 시간 기준으로 정렬
count = 0 # 몇 개 회의실 들어가는지
end = -1

for i in range(N): #
    if A[i][1] >= end: # 겹치지 않는 다음 회의가 나오는 경우 = 종료 시간 이후 회의 시작이 가능
        end = A[i][0] # 종료 시간을 업데이트
        count +=1
print(count)
"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
=4
"""