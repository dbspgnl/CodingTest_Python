# 구멍이 뚫린 게임 보드 아차원 배열과, 조각 모양을 표현하는 이차원 배열이 주어진다.
# 조각 모양이 겹치지 않게 해서 최대한 게임 보드에 넣는 방법 구하기.
# 조각은 회전이 가능하다 ...
# 조각끼리 겹치지 않아야 하기 때문에 최대 크기 계산도 해야한다.

from collections import defaultdict, deque

dx,dy = [1,0,-1,0],[0,1,0,-1]

def search(x,y,map_list,visited, mode=1): # 탐색 처리
    result = [(0,0)]
    visited[y][x] = True
    n = len(map_list)
    q = deque([(0,0)])
    while q:
        mx, my = q.popleft()
        for k in range(4):
            nx, ny = x + mx + dx[k], y + my + dy[k]
            if -1 < nx < n and -1 < ny < n and map_list[ny][nx] == mode and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((mx + dx[k], my + dy[k]))
                result.append((mx + dx[k], my + dy[k]))
    return result

def rotate_list(lst): # 회전 형태 모두 구하기
    result = [lst.copy()]
    for k in range(3):
        temp = list()
        for x, y in result[-1]:
            temp.append((-y, x))
        result.append(temp)
    return result

def make_piece_list(map_list): # 조각 형태 리스트로 담기
    n = len(map_list)
    visited = [[False]*n for _ in range(n)]
    result = list()
    for i in range(n):
        for j in range(n):
            if map_list[i][j] and not visited[i][j]:
                temp = search(j,i,map_list,visited)
                temp_size = len(temp)
                result.append([temp_size]+rotate_list(temp))
    return result

def is_inside(map_list, piece, x, y):
    n = len(map_list)
    for px, py in piece:
        nx, ny = x + px, y + py
        if nx < 0 or ny < 0 or nx >= n or ny >= n or map_list[ny][nx]:
            return False
    return True

def dfs(piece_list, map_list):
    n = len(map_list)
    m = len(piece_list)
    piece_visited = [False]*m
    visited = [[False]*n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] or map_list[i][j]:
                continue
            empty_list = search(j,i,map_list, visited, 0)
            empty_size = len(empty_list)
            for ex, ey in empty_list:
                flg = False
                x,y = j + ex, i + ey

                for k in range(m):
                    if piece_visited[k]:
                        continue
                    piece_size = piece_list[k][0]
                    if piece_size != empty_size:
                        continue

                    for _piece in piece_list[k][1:]:
                        if is_inside(map_list, _piece, x, y):
                            result += piece_size
                            piece_visited[k] = True
                            flg = True
                            break
                    if flg:
                        break
                if flg:
                    break
    return result

def solution(game_board, table):
    piece_list = make_piece_list(table)
    answer = dfs(piece_list, game_board)
    return answer


print(solution([[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]],[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]))
# 14
print(solution([[0,0,0],[1,1,0],[1,1,1]],[[1,1,1],[1,0,0],[0,0,0]]))
#0