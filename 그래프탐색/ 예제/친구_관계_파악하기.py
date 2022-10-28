"""
사람이 N명 주어지고, 관계 수가 M 주어진다. = 노드/엣지
시간복잡도는 5~2000 / 1~2000 이므로 비교적 넉넉하다.
O(V+E) * N = (2000+2000)*2000 = 8,000,000
두 번째 줄부터는 관계를 알려준다. (관계 수 만큼)
따라서 사람(노드)에 대한 관계를 담은 인접리스트로 구하면 된다.
N만큼 재귀하면서 DFS를 구한다.

프린트: 친구 관계가 다섯 단계까지(뎁스5) 존재한다면 1을 출력 아니면 0
"""

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N,M = map(int, input().split())
arrive = False
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def DFS(now, depth):
    global arrive
    if depth == 5: # 관계가 다섯까지 이어진다면 해당하는 것으로 종료
        arrive = True # 존재한다.
        return
    visited[now] = True # N번 노드는 방문 처리하고 시작한다.
    for i in A[now]: # 인접리스트 처리 # N번 노드의 엣지를 꺼낸다.
        if not visited[i]: # 방문하지 않았으면 = False이면
            DFS(i, depth+1) # 더 깊이 들어간다 = 깊이우선탐색
    visited[now] = False # 방문 처리가 없어서 끝나면 False

for _ in range(M): # 인접리스트 저장
    s, e = map(int, input().split())
    A[s].append(e) # 양방향 엣지이므로 각각 넣어준다.
    A[e].append(s)

for i in range(N):
    DFS(i, 1)
    if arrive: # 마지막까지 도달하면 true로 해줬을 것이다.
        break # 반복문 탈출

# 출력
if arrive: print(1)
else: print(0)

"""
5 4
0 1
1 2
2 3
3 4
=1
6 5
0 1
0 2
0 3
0 4
0 5
=0
6 5
0 1
0 2
0 3
0 4
0 5
=0
"""