"""
몇 번 테스트 할 지 N이 주어지고, 각 테스트 시작에 노드와 엣지의 값을 입력 받는다.
이때 이분그래프 여부를 체크하여 YES / NO을 출력하시오.
- 이분그래프: 각 집합에 속한 노드끼리 서로 인접하지 않는 두 집합으로 그래프의 노드를 나눌 수 있는 그래프
(예들 들어 집합 A,B로 방문 순서 1,2,3,4 노드를 불러서 1=A, 2=B, 3=A로 배분하고 4노드가 이미 집합이 정해진
2번 노드로 향한다면 이분 그래프가 불가능 한 것으로 NO이다.)
- 부분 요소 그룹을 체크하기 위해 DFS로 한다.
- 인접 리스트
- 방문 리스트
- 집합 저장 리스트
- 결과 변수
"""
# 백준: 1707
import sys
input = sys.stdin.readline
N = int(input())
result = True
# DFS
def DFS(node):
    global result
    visited[node] = True
    for i in A[node]:
        if not visited[i]:
            check[i] = (check[node]+1)%2 # 집합을 두 분류로 나눔
            DFS(i)
        elif check[node] == check[i]:
            result = False
# 케이스 반복
for _ in range(N):
    V, E = map(int, input().split())
    A = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    check = [0] * (V+1)
    result = True
    # 인접 리스트 저장
    for i in range(E):
        Start, End = map(int, input().split())
        A[Start].append(End)
        A[End].append(Start)
    # 주어진 그래프가 항상 1개가 아니므로 모든 노드에서 수행
    for i in range(1, V+1):
        if result:
            DFS(i)
        else:
            break
    if result:
         print("YES")
    else:
        print("NO")
"""
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
=
YES
NO
"""