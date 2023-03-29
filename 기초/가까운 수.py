import numpy
def solution(array, n):
    array = sorted(array)
    np = list(map(abs, numpy.array(array)-n))
    minv = min(np)
    idx = np.index(minv)
    return array[idx]

print(solution([3,10,28], 20)) # 28
print(solution([10,11,12], 13)) # 12
print(solution([12, 3, 4, 10, 13], 11)) # 10
# 가장 가까운 수가 여러 개일 경우 더 작은 수를 return 합니다.

"""
# 람다식
solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]

def solution(array, n):
    array.sort(key = lambda x : (abs(x-n), x-n))
    answer = array[0]
    return answer
"""