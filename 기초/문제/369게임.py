def solution(order):
    return sum(1 for i in str(order) if i == "3" or i == "6" or i =="9")

print(solution(3)) #1
print(solution(29423)) #2

"""
def solution(order):
    answer = len([1 for ch in str(order) if ch in "369"])
    return answer
    
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))    
"""