"""
방향이 없는 그래프가 주어졌을 때 연결 요소 개수를 구하자.
노드의 개수 N < 1000
엣지의 개수 M < 1000*(999)/2 = 499500

출력: 첫번째 노드와 연결된 엣지의 개수
두번째 라인부터 시작점 끝점

1. 아이디어: 그래프이면서 첫번째 노드와 연결된 모든 엣지라면 깊이탐색 사용
2. 시간복잡도: n이 1000이하이므로 n^2 모든 알고리즘 가능
3. 자료구조
인접리스트 A / 방문리스트 chk
노드 개수 n / 엣지 개수 m
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n+1)] # 배열 형태의 리스트
chk = [False] * (n+1) # 체크 false로 세팅

def DFS(v):
    chk[v] = True # 해당 인덱스 방문 처리
    for i in A[v]: # 해당 인덱스의 배열 리스트
        if not chk[i]:
            # 해당 인덱스에 연결된 엣지들을 모두 확인하면서 해당 엣지에 노드를 방문한 적이 없으면 계속 찾는다.
            DFS(i)

for _ in range(m): # 엣지만큼 체크
    s, e = map(int, input().split()) # 시작과 끝
    A[s].append(e) # 양방향 엣지이므로 양쪽에 엣지를 더한다.
    A[e].append(s)
count = 0

for i in range(1, n+1):
    if not chk[i]:
        count +=1
        DFS(i)

print(count)



"""
6 5
1 2
2 5
5 1
3 4
4 6
= 2

6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
= 1
"""