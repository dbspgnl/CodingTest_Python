# 전체 영역은 -1로 세팅하고 각각 사각형 좌표가 주어지면 내부는 0, 라인(길)은 1로 한다.
# 사각형이 동일 라인 선상에 없게 겹쳐짐으로 결국 여러 개의 직선 길로 만들어진다.
# 길은 동일 선상은 없지만 격차가 1인 경우 구분이 안됨으로 좌표를 2배해서 처리한다. (마치 테두리 생긴 것 처럼)
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    size = 50*2
    maps = [[-1] * size for i in range(size)]
    visited = [[1] * size for i in range(size)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    # 직사각형 배열 하나씩 꺼내서 맵에 그리기
    for r in rectangle:
        x1,y1,x2,y2 = map(lambda x:x*2, r) # 좌표 위치 2배 늘림
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2: # 내부는 0
                    maps[i][j] = 0
                elif maps[i][j] != 0: # 테두리(길)는 1
                    maps[i][j] = 1

    q = deque()
    q.append([characterX*2, characterY*2]) # 초기화
    while q:
        x,y = q.popleft()
        if x == itemX * 2 and y == itemY * 2: # 종료 조건
            answer = visited[x][y] //2 # 좌표 2배 했으므로 다시 2배 나눠줌.
            break
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if maps[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1
    return answer

# 사각형 좌표점 배열, 캐릭터 위치 (x,y), 아이템 목표 위치 (x,y).
print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8)) # 17
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]],9,7,6,1)) # 11
print(solution([[1,1,5,7]],1,1,4,7)) # 9
print(solution([[2,1,7,5],[6,4,10,10]],3,1,7,10)) # 15
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]],1,4,6,3)) # 10