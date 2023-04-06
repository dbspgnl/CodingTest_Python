from collections import deque
def solution(arr):
    s = deque()
    s.append(arr[0])
    for i in arr:
        if s[-1] != i:
            s.append(i)
    return list(s)

print(solution([1,1,3,3,0,1,1])) # [1,3,0,1]
print(solution([4,4,4,3,3])) #[4,3]