"""
플루이드: 모든 노드에서 다른 모든 노드까지 가는데 최소 비용, O(V^3) = 거치는 노드 * 시작노드 * 끝노드
다익스트라: 한 노드 -> 다른 모든 노드, O(ElgV)
= 다익스트라는 시작점이 있는데 플루이드는 모든 노드가 시작점이 될 수 있다.

모든 경우를 체크하다보니 행렬형 (간선)비용 이중 배열을 만든다.

1. 아이디어
- 모든 점 -> 모든 점 : 플로이드
- 비용 배열 INF 초기화
- 간선의 비용 대입
- 거쳐서 비용 줄어들 경우, 갱신(for문 3번)

2. 시간복잡도 : 플로이드 : O(V^3) > 1e6가능

3. 변수
- 비용 배열, int[][]

"""

import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
rs = [[INF] * (n+1) for _ in range(n+1)] # 거리 배열

for i in range(1, n+1): rs[i][i] = 0 # 자기 자신으로 가는 것은 0으로 고정
for i in range(m):
    a,b,c, = map(int, input().split()) # 간선 처리 # a에서 b로 c비용으로 이동
    rs[a][b] = min(rs[a][b], c) # 하나에 여러 간선이 있을 수 있으므로 최소값만 넣어준다.

for k in range(1, n+1): # 거치는 값
    for j in range(1, n+1): # 시작
        for i in range(1, n+1): # 끝
            if rs[j][i] > rs[j][k] + rs[k][i]: # 시작에서 끝으로 가는게 > 거치는 거랑 끝으로 가는 것보다 크면
                rs[j][i] = rs[j][k] + rs[k][i] # 갱신 = 거치고 가는데도 그게 더 기존 길보다 작은 경우 그걸로 교체

for j in range(1, n+1):
    for i in range(1, n+1):
        if rs[j][i] == INF: print(0, end=' ')
        else: print(rs[j][i], end=' ')
    print()

"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
=0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0
"""