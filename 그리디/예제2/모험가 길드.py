"""
N명의 모험가는 각각 공포도를 가지고 있다.
공포토가 X인 모험가는 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
모든 모헙가를 여행에 보낼 필요는 없다.
여행을 떠날 수 있는 최대 그룹 수는?
- 오름차순으로 해서 그룹핑한다.
"""
n = int(input())
data = list(map(int, input().split()))
data.sort()
result = 0 # 총 그룹 수
count = 0 # 그룹에 모험가 수
for i in data: # i는 공포도
    count += 1
    if count >= i: # 멤버수가 공포도보다 높으면
        result +=1
        count = 0 # 초기화
print(result)
"""
5
2 3 1 2 2
= 2
"""