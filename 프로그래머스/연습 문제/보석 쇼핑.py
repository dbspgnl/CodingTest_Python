# 보석 배열이 주어질 때, 모든 보석이 포함되게 하는 최단 거리 인덱스 구하기
def solution(gems):
    n = len(gems)
    answer = [0, n-1] # 모든 범위
    kind = len(set(gems)) # 보석 종류 (중복 제거)
    dic = {gems[0]:1} # 첫번째 보석 담기
    start, end = 0,0
    while start<n and end<n: # 처음부터 끝까지 탐색
        if len(dic) < kind: # 종류가 부족하면 end 늘려서 범위 확대
            end +=1
            if end == n: # 범위에 다다르면 멈춤
                break
            dic[gems[end]] = dic.get(gems[end], 0)+1 # 해당 딕셔너리 갱신
        else: # 종류 충족
            if (end-start+1) < (answer[1]-answer[0]+1):
                answer = [start, end] # 충족한 범위가 기록 범위보다 작으면 갱신
            if dic[gems[start]] == 1:
                del dic[gems[start]] # 이미 충족된 상태면 기록 후 구단 단축을 위해서 제거
            else:
                dic[gems[start]] -= 1 # 제거할 수 없으면 감소
            start += 1
    answer[0] +=1 # 인덱스 1부터 시작
    answer[1] +=1
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) #[3, 7]
print(solution(["AA", "AB", "AC", "AA", "AC"])) #[1, 3]
print(solution(["XYZ", "XYZ", "XYZ"])) #[1, 1]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) #[1, 5]