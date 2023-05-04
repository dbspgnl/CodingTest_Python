def solution(hp):
    answer = 0
    answer += hp // 5
    answer += (hp % 5) // 3
    answer += (hp % 5) % 3
    return answer

print(solution(23)) # 5
print(solution(24)) # 6
print(solution(999)) # 201

"""
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
"""
