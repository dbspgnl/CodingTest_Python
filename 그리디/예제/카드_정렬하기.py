"""
카드 뭉치를 최소로 합치는 방법에 대한 문제.
뭉치의 종류가 주어지고 그 안에서 최선을 구하는 문제 = 그리디
N = 카드 뭉치의 수
pa = 뭉치의 크기를 담는 우선순위 큐 (자동 정렬)
** 작은 뭉치부터 합쳐야 비교 횟수가 적어진다.
(10+20)=30 > 30+(30+40) = 100
(10+40)=50 > 50+(50+20) = 120
"""
from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N): # 카드 뭉치 담기
    date = int(input())
    pq.put(date)
data1= 0
data2= 0
sum= 0

# 우선순위 큐는 데이터를 자동 정렬한다.
while pq.qsize()>1:
    data1 = pq.get() # 작은 수 두개
    data2 = pq.get()
    temp = data1+data2 # 합친 값이 하나의 새로운 뭉치
    sum += temp # 총 개수에 더한다
    pq.put(temp) # 새로운 뭉치를 다시 뭉치 리스트에 넣음
print(sum)
"""
3
10
20
40
=100
"""