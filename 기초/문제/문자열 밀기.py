from collections import deque
def solution(A, B):
    q = deque(A)
    for i in range(len(A)):
        if "".join(q) == B:
            return i
        q.rotate(1)
    return -1

print(solution("hello","ohell")) # 1
print(solution("apple","elppa")) # -1

"""
solution=lambda a,b:(b*2).find(a)
"""