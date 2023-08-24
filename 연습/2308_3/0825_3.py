# 보석 배열이 주어질 때, 모든 보석이 포함되게 하는 최단 거리 인덱스 구하기
def solution(gems):
    n = len(gems)
    answer = [0, n-1]
    kind = len(set(gems)) # 보석 종류
    dic = {gems[0]:1} # 첫번째 담고 카운팅 1
    start, end = 0,0
    while start<n and end<n:
        if len(dic) < kind: # 보석 부족
            end +=1
            if end == n:
                break
            dic[gems[end]] = dic.get(gems[end], 0)+1 # 카운팅
        else: # 보석 조건 해당
            if (end-start+1)<(answer[1]-answer[0]+1): # 답보다 작으면 답 갱신
                answer = [start, end]
            if dic[gems[start]] ==1: # 1이면 없애고
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1 # 카운팅
            start +=1
    answer[0] +=1
    answer[1] +=1
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) #[3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) #[1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) #[1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) #[1, 5]