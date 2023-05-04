# def dfs(y, x):
#     for k in range(6):
#         ny = y + dy[k]
#         nx = x + dx[k]
#         if 0 <= ny < n and 0 <= nx < n:
#             map[ny][nx] = 1

def solution(board):
    map = board.copy()
    n = len(board[0]) # 5
    target = []
    # y,x = 0,0
    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                # y,x = i,j # 3,2
                target.append((i,j))
    print(target)
    for y,x in target:
        for k in range(9):
            ny = y + dy[k]
            nx = x + dx[k]
            print("---")
            print(ny)
            print(nx)
            if 0 <= ny < n and 0 <= nx < n:
                map[ny][nx] = 1
    for m in board:
        print(m)
    return (n*n) - sum(sum(a) for a in map)

print(solution(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
)) # 16

print(solution(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
)) # 13

"""
# 깔금한 코드... 근데 너무 파이썬스럽다.
def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di in [-1,0,1] for dj in [-1, 0, 1])
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)
"""