"""
주어진 문자열 사이로 덧셈 또는 곱셈을 이용해서 가장 큰 수로 만들기.
보통은 곱하기가 유리하나, 두 수 중 하나가 0이거나 1이면 더하기를 해야한다.
"""
data = input()
result = int(data[0]) # 첫번째값 세팅
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)
"""
02984
= 576
567
= 210
"""