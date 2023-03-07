"""
# 노드, 비교 횟수
# 0이면 합하고 1이면 조회
# 0 1 3: 1과 3을 합침
# 1 1 7: 1과 7이 같은 집합인지?
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
# 1일 때 집합이면 YES 아니면 NO
"""
# 유니온 파인드
n,m = map(int, input().split())
parent = [0]*(n+1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def chk(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    else:
        return False

for i in range(1, n+1):
    parent[i] = i

for i in range(m):
    q,a,b = map(int, input().split())
    if q == 0:
        union(a,b)
    else:
        if chk(a,b):
            print("YES")
        else:
            print("NO")