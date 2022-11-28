"""
원소의 개수 N과 연산 횟수 M이 주어진다. (각각 10만 이하)
이후 합집합 요소가 0 a b 형태로 주어진다.
0는 a가 포함되어 있는 집합과 b가 포함되어 있는 집합을 합친다는 의미이다. (유니온)
1은 a와 b가 포함돼 있는지를 확인하는 연산이다.
a,b는 N이하의 자연수이다.
a와 b가 같은 집합에 포함되어 있으면 YES 아니면 No를 출력한다.
- 대표 노드 저장 리스트
- find 연산 함수 / union 연산 함수 / 집합 체크 여부 함수
"""
# 백준: 1717
N, M = map(int, input().split())
parent = [0] * (N+1) # 대표노드 저장
# find
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 추적
        return parent[a]
# union
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
# check
def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False

for i in range(0, N+1): # 대표노드 초기 세팅
    parent[i] = i

for i in range(M): # 연산 횟수만큼 반복
    question, a, b = map(int, input().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("No")
"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
=NO
NO
YES
"""