def solution(phone_book):
    phone_book = list(set(phone_book))
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1)
        print(p2)
        return not p2.startswith(p1)

# def solution(phone_book):
#     s = dict()
#     for p in phone_book:
#         for i in range(1, len(p)):
#             s[p[:i]] = 1
#     # s = list(s) # 주석을 풀고 제출해보세요
#     for p in phone_book:
#         if p in s:
#             return False
#     return True

# 전화번호 내 접두사가 겹치면 false 없으면 true
print(solution(["119", "97674223", "1195524421"])) #false
print(solution(["123","456","789"])) #true
print(solution(["12","123","1235","567","88"])) #false
print(solution(["1195524421", "119"])) #false
print(solution(["1195524421", "1195524421"])) #false
print(solution(["00211", "001"])) #true
print(solution(["0011", "001"])) #false
print(solution(["11", "12", "111"])) #false

