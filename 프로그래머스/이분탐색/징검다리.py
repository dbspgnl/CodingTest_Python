# 이 문제가 이분탐색인 이유는 input값이 너무 크기 때문이다.
# 거리가 주어지고 그 안에 바위 위치 정보가 배열로 주어진다.
# 이 중에 n개의 바위를 제거할 때의 가장 짧은 최소 길이를 구한 뒤,
# 바위 제거의 모든 경우의 수 중에서 최소 길이가 가장 큰 값을 리턴.
def solution(distance, rocks, n):
    answer = 0
    left, right = 1, distance
    rocks.sort()
    rocks.append(distance)

    while left <= right:
        mid = (left+right)//2 # mid = target
        remove_count = 0 # 제거 바위 카운팅
        prev_rock = 0 # 이전 바위 위치
        for rock in rocks:
            interval = rock - prev_rock
            if interval < mid:
                remove_count +=1
            else:
                prev_rock = rock
            if remove_count > n:
                break
        if remove_count > n:
            right = mid -1
        else:
            answer = mid
            left = mid +1
    return answer

# 거리, 바위 위치, 제거할 바위 수
print(solution(25, [2, 14, 11, 21, 17], 2)) # 4
# sort = 2, 11, 14, 17, 21 (간격 9,3,3,4)
'''
mid와 거리를 아예 따로 생각해야 한다. 
mid는 타겟을 서치하기 위한 값일 뿐이다.
즉, 25길이의 절반인 12는 예상하는 값의 추정일 뿐이다.
1. 제거할 때의 간격(interval)이 얼마나 되는가?
이 문제도 n (제거 횟수)가 중요하다. 
바위 간의 간격이 mid(타겟)보다 작으면 카운팅이 되서 초과해버린다.
처음 mid=12는 모든 간격보다 작기 때문에 답이 아니다.
이후 mid=5는 세 군데나 작기 때문에 목표 n=2가 아니라 역시 아니다.
이후 mid=2는 모든 간격에 해당되기 때문에 답의 가능성을 가진다.
하지만 우리 목표는 가장 작은 값을 구하는 것이 아니라 조건에 해당하는 가장 작은 값 중 최고 값이다.
따라서 left를 늘려나가면서 조건에 해당되는한 계속 최소값을 올려줘야 한다. 
2. left를 올려가면서 right에 도달할때까지 연산
이제 right는 4로 고정되고 (mid=2는 answer가 되고, 직전 right는 mid=5-1이었기 때문에)
left는 임시로 구한 답 left=2에서 while문에 의해서 left가 right가 될때까지
left+1에 의해서 답을 찾아간다. 
'''