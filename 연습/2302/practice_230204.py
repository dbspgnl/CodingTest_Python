import sys
import heapq
input = sys.stdin.readline
v,e = map(int, input().split())
edgeList = [[] for _ in range(v+1)]
chk = [False] * (v+1)
rs = 0
for i in range(e):
    a,b,w = map(int, input().split())
    edgeList[a].append([w,b])
    edgeList[b].append([w,a])
heap = [[0,1]] # 시작점 v
while heap: # 배열 세팅
    w, ev = heapq.heappop(heap) # 힙에서 배열 꺼내기
    print("w: ", w)
    print("ev: ", ev)
    if chk[ev] == False: # 꺼낸 노드가 체크
        chk[ev] = True # 꺼낸 노드 체크 표시
        rs += w # 꺼낸 노드에 거리 처리
        for nextEdge in edgeList[ev]: # 꺼낸 노드의 엣지 리스트 정보를 가져옴
            if chk[nextEdge[1]] == False: # 꺼낸 노드의 엣지 리스트의 노드 = 다음 노드가 아직 방문 아니면
                heapq.heappush(heap, nextEdge) # heap 배열에 nextEdge[] 넣기
print("rs: ", rs)
