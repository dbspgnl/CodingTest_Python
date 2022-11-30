"""
사람 수 N과 파티의 개수 M이 주어진다.
그 다음 진실을 아는 사람 수와 해당 사람 정보가 주어진다. 0이면 한 번만 주어진다.
이후 3번째 줄부터 파티 인원과 각 파티 인원 맴버 정보가 들어온다.
이때 정보를 아는 사람이 포함되지 않은 파티 수는 몇 개인가?
"""
# 백준: 1043
N, M = map(int, input().split())
trueP = list(map(int, input().split()))
T = trueP[0]
del trueP[0]
result = 0
party = [[] for _ in range(M)]
# find
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
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
# 파티 데이터 입력받기
for i in range(M):
    party[i] = list(map(int, input().split()))
    del party[i][0]
parent = [0]*(N+1)
# 대표 노드 초기 설정 (자기자신)
for i in range(N+1):
    parent[i] = i
# 각 파티 사람들을 1개의 그룹으로 유니온
for i in range(M):
    firstPeople = party[i][0]
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])
# 정보 아는 사람 체크
for i in range(M):
    isPossible = True
    firstPeople = party[i][0]
    for j in range(len(trueP)):
        if find(firstPeople) == find(trueP[j]):
            isPossible = False
            break
    if isPossible:
        result +=1 # 모두 다르면 아무도 모름 = +1
print(result)
"""
4 5
1 1
1 1
1 2
1 3
1 4
2 4 1
= 2
"""