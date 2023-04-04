# def solution(phone_book):
#     phone_book = list(set(phone_book))
#     phone_book.sort()
#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         print(p1)
#         print(p2)
#         return not p2.startswith(p1)

# 이 문제의 핵심은 접두사를 찾는건데 자기 자신 자체가 접두사가 되면 안되는 문제가 있다.
# 따라서 그냥 생각없이 앞부분만 떼어내면 실패한다.
# 아래와 같이 딕셔너리로 직전까지만 담아서 새로 배열로 만든 후 포함 여부를 판단해야한다.
# def solution(phone_book):
#     s = dict() # list 슬라이스 안된다.
#     for p in phone_book:
#         for i in range(1, len(p)):
#             s[p[:i]] = 1
#     # s = list(s) # 다시 배열로 만들면 탐색 과정에서 길어서 효율성에서 탈락해버림....
#     for p in phone_book:
#         if p in s:
#             return False
#     return True

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number: # 나랑 동일하면 안됨
                answer = False
    return answer

# 전화번호 내 접두사가 겹치면 false 없으면 true
print(solution(["119", "97674223", "1195524421"])) #false
print(solution(["123","456","789"])) #true
print(solution(["12","123","1235","567","88"])) #false
print(solution(["1195524421", "1195524421"])) #true
print(solution(["1", "11"])) #false

