from collections import Counter
def solution(want, number, discount):
    answer = 0
    check = {}
    # 두 배열 하나의 딕셔너리로 묶기
    for w, n in zip(want, number):
        check[w] = n
        
    for i in range(len(discount)-9): # 범위 초과 제외     
        c = Counter(discount[i:i+10]) 
        print(c)
        if c == check: # 일치하는 딕셔너리
            answer +=1
                
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])) # 3
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])) # 0
