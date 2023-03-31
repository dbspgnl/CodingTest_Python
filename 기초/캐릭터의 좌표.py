def solution(keyinput, board):
    me = [0,0]
    x = int((board[0]-1)/2)
    y = int((board[1]-1)/2)
    key = {"left":[-1,0], "right":[1,0], "up":[0,1], "down":[0,-1]}
    for input in keyinput:
        me[0] += key[input][0]
        me[1] += key[input][1]
        if -x > me[0]: me[0] = -x
        if x < me[0]: me[0] = x
        if -y > me[1]: me[1] = -y
        if y < me[1]: me[1] = y
    return me

print(solution(["left", "right", "up", "right", "right"],[11, 11])) # [2,1]
print(solution(["down", "down", "down", "down", "down"],[7, 9])) # [0,-4]
print(solution(["left", "left", "left", "left", "right", "right", "right", "right"],[5, 5])) # [2,0]