# def solution(numlist: list, n: int) -> list:
#     return sorted(numlist, key=lambda x: (abs(n-x), -x))
"""
# 정답 실패: abs 같은 거리라도 양수끼리 클 때는 적용되지만 음수vs양수일 땐 바뀌기 때문에 안됨
def solution(numlist, n):
    answer = []
    numlist.reverse()
    print(numlist)
    dist = list(enumerate([i-n for i in numlist]))
    # dist = dict(zip('abcd', range(5)))
    print(dist)
    swap = [(i[1],i[0]) for i in dist] # key와 value 변경
    for i in range(len(numlist)):
        print(swap)
        print(min(swap)[0]) # v
        print(min(swap)[1]) # k
        answer.append(numlist[min(swap)[1]])
        swap[min(swap)[1]] = (9999, min(swap)[1])
    return answer
    
>>>


"""
def solution(numlist, n):
    # num -> (abs(n-num), -num)
    numlist = [(abs(n-num), -num) for num in numlist] # 오름차순을 위해서 -를 사용...
    # 첫 번째 요소를 기준으로 오름차순 정렬 and 두 번째 요소를 기준으로 내림차순 정렬
    numlist.sort()
    print(numlist)
    # 두 번쨰 요소만 반환
    return [-num for _, num in numlist]

# print(solution([1, 2, 3, 4, 5, 6], 4)) # [4, 5, 3, 6, 2, 1]
print(solution([600, 400, 300, 200, 700, 800, 100, 900], 500)) # [600, 400, 700, 300, 800, 200, 900, 100]
