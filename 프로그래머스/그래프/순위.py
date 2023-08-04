# 플로이드 워셜
# 주어진 조건이 많지 않다.
from collections import Counter
def solution(n, result):
    board = [[0] * n for _ in range(n)]
    for p1, p2 in result:
        board[p1-1][p2-1] = 1 # p1가 p2에게 이김 p1>p2
        board[p2-1][p1-1] = -1  # p2이 p1에게 짐 p2<p1
    for k in range(n):
        for j in range(n):
            for i in range(n):
                if board[i][j] == 0:
                    if board[i][k] == 1 and board[k][j] == 1:
                        board[i][j] = 1 # i>k, k>j이면 i>j이다.
                    elif board[i][k] == -1 and board[k][j] == -1:
                        board[i][j] = -1 # i<k, k<j이면 j>j이다.
    answer = 0
    for i in range(n):
        if Counter(board[i])[0] == 1:
            answer +=1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) #2