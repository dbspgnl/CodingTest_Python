# def solution(num, total):
#     S = [] # 합배열
#     temp = 0
#     for i in range(num+total+1):
#         temp = temp + i
#         S.append(temp)
#     start = 1
#     while start <= total:
#         if S[start+num] - S[start] == total:
#             return [i for i in range(start+1, start+num+1)]
#         else:
#             start +=1

def solution(num, total):
    start = 0
    answer = 0
    if num == 1: return [total]
    while True:
        for i in range(num):
            answer += start+i
        print(answer)
        if answer == total:
            return [i for i in range(start, start+num)]
        elif answer > total:
            start -=1
        else:
            start +=1
        answer = 0


print(solution(3,12))	#[3, 4, 5]
print(solution(5,15))	#[1, 2, 3, 4, 5]
print(solution(4,14))	#[2, 3, 4, 5]
print(solution(5,5))    #[-1, 0, 1, 2, 3]
print(solution(1,7))    #[7]
print(solution(3,0))    #[-1,0,1]


"""
# ?
def solution(num, total):
    return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]
"""
