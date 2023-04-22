# 투포인트 문제
def solution(people, limit):
    answer = 0
    people.sort()
    start = 0
    end = len(people)-1
    while start<end: # 가장 큰 값 작은 값 묶어서 통과하면 처리
        if people[start] + people[end] <= limit:
            start +=1
            answer +=1
        end -=1
    return len(people) - answer