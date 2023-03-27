# 직사각형 가로,세로,높이가 주어진다.
# 정육각형 길이 n이 주어질 때, 정육각형이 직사각형에 몇 개나 들어가나?

# def solution(box, n):
#     answer = 1
#     x,y,z = box
#     if n > x or n > y or n > z: return 0
#     answer *= x // n
#     answer *= y // n
#     answer *= y // n
#     return answer


def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )

print(solution([10,8,6],3)) # 12
print(solution([1,10,10],2)) # 12
