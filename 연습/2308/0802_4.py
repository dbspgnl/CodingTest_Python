n = int(input())
arr = list(map(int, input().split())) # 주어진 배열
arr.sort()
t = int(input())
tlist = list(map(int, input().split())) # 타겟

for i in range(t):
    find = False
    target = tlist[i]
    start = 0
    end = len(arr)-1
    while start <= end:
        mid_i = int((start+end)//2)
        mid_v = arr[mid_i]
        if mid_v > target:
            end = mid_i-1
        elif mid_v < target:
            start = mid_i+1
        else:
            find = True
            break
    if find: print(1)
    else: print(0)