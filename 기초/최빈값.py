from collections import Counter
def solution(array):
    count = Counter(array).most_common()
    if len(count) == 1:
        return 1
    return -1 if count[0][1] == count[1][1] else count[0][1]

print(solution([1, 2, 3, 3, 3, 4]))	#3
# print(solution([1, 1, 2, 2]))	#-1
# print(solution([1]))	#1
# print(solution([0,1,0,0,1,1]))