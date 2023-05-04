def solution(num_list):
    count = sum(1 for num in num_list if num % 2 == 0)
    return [count, len(num_list)-count]

print(solution([1, 2, 3, 4, 5]))

"""
# 나머지를 인덱스로 이용해서 카운팅하는 방식
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
"""