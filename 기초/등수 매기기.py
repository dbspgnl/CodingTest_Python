def solution(score):
    answer = []
    avg = [sum(i)/2 for i in score] # 평균으로 새로 배열화
    avgList = sorted(avg, reverse=True) # 평균을 내림차순 정렬
    for i in avg:
        answer.append(avgList.index(i)+1) # !핵심은 동률일 때 앞에 인덱스가 적용된다는 점.
    return answer # [100, 95, 90, 90, 80]에서 90점으로 인덱스를 찾으면 앞 인덱스가 두 번 적용된다.

print(solution([[80, 70], [90, 50], [40, 70], [50, 80]])) # [1,2,4,3]
print(solution([[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]])) # [4, 4, 6, 2, 2, 1, 7]

"""
def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]
"""
