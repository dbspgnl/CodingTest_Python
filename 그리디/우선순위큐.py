# 그리드 알고리즘은 최선 선택을 반복하는 알고리즘이기 때문에 우선순위 큐를 많이 사용한다.

# PriorityQueue
from queue import PriorityQueue
myque = PriorityQueue() # 우선순위 큐 생성
# 기본함수
data = 1
myque.put(data) # 원소 추가
myque.get(1) # 큐에서 데이터 꺼내기
myque.qsize() # 큐 사이즈 가져오기
myque.empty() # 큐 비어있는지 확인

# heapq
import heapq
mylist = []
heapq.heappush(mylist, 1) # 데이터(1)을 리스트 형태로 저장
heapq.heappop(mylist) # 리스트에서 데이터 꺼내기
heapq.heapify(mylist) # 리스트를 heap 자료구조로 변환