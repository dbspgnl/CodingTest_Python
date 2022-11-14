"""
임의의 수열이 주어진다. 수열의 합을 구하기 전에 두 쌍씩 묶어서 곱한 뒤 전체 합을 구한다.
그 합이 최대가 되는 수는?
유형을 나눈다.
이 규칙에서 최대 값은 높은 수끼리 곱하는 것이다.
1. 1보다 큰 양수 / 2. 1의 개수 / 3. 0의 개수 / 4. 음수
- 1번을 모두 더한다.
- 4번에서 두 쌍 묶다가 마지막 하나가 남을 경우 다음을 시행한다.
- 수열에 0이 있으면 남은 음수와 곱한다.
- 수열에 0이 없으면 그대로 음수를 더한다.
- 남아있는 2번(1의 개수를 더한다) = 1은 곱하는 것은 의미가 없다. 더하는 게 낫다.
N = 수열의 수
plusPq = 양수 우선순위 큐
minusPq = 음수 우선순위 큐
one = 1의 개수 카운트
zero = 0의 개수 카운트
"""
from queue import PriorityQueue
N = int(input())
plusPq = PriorityQueue()
minusPq = PriorityQueue()
one = 0
zero = 0

for i in range(N):
    data = int(input())
    if data >1:
        plusPq.put(data*-1) # 내림차순 정렬 > 대신 꺼낼 때 *-1
    elif data ==1:
        one +=1
    elif data ==0:
        zero +=1
    else:
        minusPq.put(data)
sum=0
#양수 처리
while plusPq.qsize()>1: # 1하나가 남을 동안 반복
    first = plusPq.get()*-1
    second = plusPq.get()*-1
    sum += first*second
if plusPq.qsize() > 0: # 나머지 하나를 더해줌
    sum += plusPq.get()*-1
#음수 처리
while minusPq.qsize()>1: # 하나가 남을 동안 반복
    first = minusPq.get()
    second = minusPq.get()
    sum += first*second
if minusPq.qsize() > 0: # 나머지 하나 처리
    if zero == 0: # 0이 없으면
        sum += minusPq.get() # 걍 더해준다.
sum += one # 남은 1 모두 더해주기
print(sum)
"""
6
0
1
2
4
3
5
= 27
"""