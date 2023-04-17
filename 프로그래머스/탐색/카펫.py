# brown + yellow = x*y
# x >= y
# yello가 같더라도 brown에 따라 가로가 달라짐
#
def solution(brown, yellow):
    answer = []
    x = 0
    y = 0
    for i in range(1, yellow+1):
        if yellow % i == 0: # 가로x세로 조건
            x = int(yellow/i)
            y = i
            if (2*x) + (2*y) + 4 == brown: # 옐로우 가로 세로 + 모서리
                answer.append(x+2) # 브라운은 옐로보다 2칸 더 길다
                answer.append(y+2)
                return answer
    return answer


print(solution(10,2)) # [4, 3]
print(solution(8,1)) # [3, 3]
print(solution(24,24)) # [8, 6]
print(solution(12,3)) # [5, 3]
print(solution(16,9)) # [5, 5]
print(solution(24,9)) # [11, 3]
