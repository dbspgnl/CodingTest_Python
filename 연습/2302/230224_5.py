"""
# 배열 길이
# 주어진 배열
# 찾을 수
# 찾을 수 배열
5
4 1 5 2 3
5
1 3 7 9 5
= 1
1
0
0
1
# 찾을 수 만큼 체크하여 찾을 수가 있으면 1, 없으면 0
"""
# 이진탐색
a = int(input())
aList = list(map(int, input().split()))
aList.sort() # 이진탐색은 반드시 정렬해줘야 한다...
t = int(input())
tList = list(map(int, input().split()))

for i in range(t):
    start = 0
    end = len(aList)-1
    target = tList[i]
    find = False
    while start <= end:
        mi = int((start+end)//2)
        mv = aList[mi]
        if mv > target:
            end = mi-1
        elif mv < target:
            start = mi+1
        else:
            find = True
            break
    if find: print(1)
    else: print(0)
