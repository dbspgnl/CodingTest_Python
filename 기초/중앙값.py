def solution(array):
    array.sort()
    return array[int(len(array)//2)]

"""
def solution(array):
    return sorted(array)[len(array) // 2]
"""