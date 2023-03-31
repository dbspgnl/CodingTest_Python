def solution(id_pw, db):
    id, pw = id_pw
    for data in db:
        if id in data:
            if pw == data[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"

print(solution(["meosseugi", "1234"],[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]])) # "login"
print(solution(["programmer01", "15789"],[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]])) #"wrong pw"
print(solution(["rabbit04", "98761"],[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]])) # "fail"

"""
# 참고용
def solution(id_pw, db):
    if db_pw := dict(db).get(id_pw[0]):
        return "login" if db_pw == id_pw[1] else "wrong pw"
    return "fail"
# =:는 바다코끼리 연산자라고 부른다.
# 	if result := 'walrus' in (s := 'walrus eat kimchi'):
#     print(result) # true
"""