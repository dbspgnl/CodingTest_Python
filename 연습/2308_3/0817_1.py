# 보석 배열이 주어질 때, 모든 보석이 포함되게 하는 최단 거리 인덱스 구하기
def solution(gems):
    n = len(gems) # 끝
    answer = [0, n-1]
    kind = len(set(gems)) # 종류
    dic = dict({gems[0]:1})
    start, end = 0,0
    while start<n and end<n:
        if len(dic) < kind:
            end +=1
            if end == n: # 끝
                break
            dic[gems[end]] = dic.get(gems[end], 0)+1 # 꺼낸 뒤 +1
        else: # 종류 충족
            if (end-start+1) < (answer[1]-answer[0]+1):
                answer = [start, end] # 더 낮은 값으로 갱신
            if dic[gems[start]] == 1:
                del dic[gems[start]] # 하나 남으면 키 삭제
            else:
                dic[gems[start]] -= 1 # 하나 이상이면 감소
            start +=1
    answer[0] +=1 # 인덱스+1
    answer[1] +=1
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) #[3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) #[1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) #[1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) #[1, 5]