"""
# 처음 풀었을 때 예제는 풀리는데 전체 예제에서 계속 실패가 발생함
from collections import Counter
def solution(array):
    count = Counter(array).most_common()
    if len(count) == 1:
        return 1
    return -1 if count[0][1] == count[1][1] else count[0][1]

"""
def solution(array):
    # print(set([1, 2, 3, 3, 3, 4]))
    while len(array) !=0:
        print(">")
        for i, a in enumerate(set(array)):
            array.remove(a)
            print(array)
        if i==0: return a
    return -1

print(solution([1, 2, 3, 3, 3, 4]))	#3
print(solution([1, 1, 2, 2]))	#-1 아마도 여기서 문제가 발생?
print(solution([1]))	#1

