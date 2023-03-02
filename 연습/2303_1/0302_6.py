"""
# 노드 수 / 인접 정보 받기
# 인접 리스트 받기
4 2
4 2
3 1
= 4 2 3 1 or 3 4 1 2
# 두번째 예시
10 4
1 3
2 6
3 6
5 9
= 1 2 4 5 7 8 10 3 9 6
"""
# 위상정렬, 덱을 사용한다.
from collections import deque
n,m = map(int, input().split())
eList = [[] for _ in range(n+1)]
inde = [0] * (n+1)

# 인접리스트 세팅
for i in range(m):
    s,e = map(int, input().split())
    eList[s].append(e)
    inde[e] += 1

# 덱 초기화 (0인 애들 넣기)
q = deque()
for i in range(1, n+1):
    if inde[i] == 0:
        q.append(i)

# 덱에 있는 것들 가져오기
while q:
    ev = q.popleft()
    print(ev, end=' ')
    for nv in eList[ev]:
        inde[nv] -=1
        if inde[nv] == 0:
            q.append(nv)