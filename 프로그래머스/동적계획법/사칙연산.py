# ["1", "-", "3", "+", "5", "-", "8"] 배열의 모든 계산 경우는 [-15, -5, -5, 1, 1]이다.
# 괄호로 인한 결합법칙 경우의 수 중에 최대값 구하기.

def solution(arr):
    minv = 0
    maxv = 0
    sumv = 0
    for idx in range(len(arr) - 1, -1, -1):
        if arr[idx] == '+':
            continue
        elif arr[idx] == '-':
            temp_min = minv
            temp_max = maxv
            minv = min(-(sumv + temp_max), -sumv + temp_min)
            minus_v = int(arr[idx + 1])
            maxv = max(-(sumv + temp_min), -minus_v + (sumv - minus_v) + temp_max)
            sumv = 0
        elif int(arr[idx]) >= 0:
            sumv += int(arr[idx])
    maxv += sumv # 첫 수는 반드시 양수이므로 더해준다
    return maxv

print(solution(["1", "-", "3", "+", "5", "-", "8"])) # 1
print((solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))) # 3

'''
뒤에서부터 계산하는 이유는 결합 법칙 특성상 마지막 수는 반드시 앞의 부호를 따르기 때문이다.
반대로 첫 수는 반드시 양수임으로 마지막에 더 해준다.
핵심은 작은 수에서 큰 수를 빼는 게 아니라, 큰 수에서 작은 수를 빼도록 처리하는 것.
'''