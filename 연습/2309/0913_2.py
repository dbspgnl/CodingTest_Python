# 징검다리.
def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance
    rocks.sort()
    # rocks.append(distance)
    while left <= right: # 최소 간격을 구할거임
        mid = (left+right)//2
        remove_count = 0
        prev_rock = 0
        for rock in rocks:
            interval = rock - prev_rock
            if interval < mid:
                remove_count +=1
            else:
                prev_rock = rock
            if remove_count > n: break
        if remove_count > n:
            right = mid -1
        else:
            answer = mid
            left = mid+1
    return answer

# 거리, 바위 위치, 제거할 바위 수
print(solution(25, [2, 14, 11, 21, 17], 2)) # 4
# sort = 2, 11, 14, 17, 21 (간격 9,3,3,4)
