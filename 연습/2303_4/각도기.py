# 90이하면 1, 90이면 2, 90초과 180미만 3, 180은 4이다.
def solution(angle):
    if angle % 90 == 0:
        return (angle//90)*2
    else:
        return 1 if angle < 90 else 3
"""
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1  
    return answer
"""
# + (angle % 90 > 0) * 1 앞의 부등호가 true 1이 되서 살아서 1이 되고 false이면 0*1되서 0이 된다.

