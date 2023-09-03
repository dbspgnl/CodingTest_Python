from collections import Counter
def solution(k, tangerine):
    answer = 0
    counted_tangerine = Counter(tangerine)
    sorted_tangerine = sorted(counted_tangerine.items(),key=lambda x:x[1],reverse=True)
    for i in sorted_tangerine:
        k -= i[1] # 첫번째 종류를 모두 뺌
        answer +=1 # 종류 카운팅
        if k <=0: break # k만큼 다 빼면 종료
    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3])) #3