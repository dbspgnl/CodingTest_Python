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
aleng = int(input())
aList = list(map(int, input().split()))
aList.sort()
tleng = int(input())
tList = list(map(int, input().split()))

for i in range(tleng):
    find = False
    t = tList[i]
    start = 0
    end = len(aList)-1
    while start <= end:
        midI = int((start+end)//2)
        midV = aList[midI]
        if midV > t: # 값이 크면 엔드 변경
            end = midI-1
        elif midV < t:
            start = midI+1
        else:
            find = True
            break
    if find: print(1)
    else: print(0)