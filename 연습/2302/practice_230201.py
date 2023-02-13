n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
target_list = list(map(int, input().split()))
for i in range(m):
    find = False # 찾으면 1 아니면 0
    target = target_list[i]
    start = 0
    end = len(a)-1
    while start <= end:
        midi = int((start+end)//2) # 중앙 인덱스
        midv = a[midi] # 중앙 값
        if midv > target:
            end = midv-1
        elif midv < target:
            start = midv+1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)


