# 이진탐색
n = int(input())
alist = list(map(int, input().split()))
alist.sort()
m = int(input())
tlist = list(map(int, input().split())) # 타겟

for i in range(m):
    find = False
    t = tlist[i]
    start = 0
    end = len(alist)-1
    while start <= end:
        midi = int((start+end)//2)
        midv = alist[midi]
        if midv > t:
            end = midi-1
        elif midv < t:
            start = midi+1
        else:
            find = True
            break
    if find: print(1)
    else: print(0)