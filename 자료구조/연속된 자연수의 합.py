"""
N을 입력받는다. 연속된 자연수가 N이 되는 경우 찾기.
15 = 1~5 / 4~6 / 7~8 / 15 = 4개
"""
n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1
while end_index !=n :
    if sum == n: # 정답인 경우
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index +=1
        sum += end_index
print(count)
"""
15
= 4
"""