# 투포인트
# 몸무게 배열과 한도가 주어질 때, 보트를 두 명씩 한다면 최소 횟수
def solution(people, limit):
    answer = 0 # 보트를 두명씩 탈 때 최소 횟수
    people.sort()
    start = 0
    end = len(people)-1
    while start < end:
        if people[start] + people[end] <= limit:
            start +=1
            answer +=1
        else:
            end -=1
    return len(people) - answer

print(solution([70, 50, 80, 50],100))	#3
print(solution([70, 80, 50],100))	#3