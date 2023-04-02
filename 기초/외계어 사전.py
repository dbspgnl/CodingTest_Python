def solution(spell, dic):
    result = []
    val = 0
    for d in dic:
        for w in spell:
            val += list(set(d)).count(w)
        result.append(val)
        val = 0
    return 1 if len(spell) in result else 2

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])) # 2 없음
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"])) # 1 있음(dzx)
print(solution(["s", "o", "m", "d"],["moos", "dzx", "smm", "sunmmo", "som"])) # 2 없음

"""
# 집합에서 집합을 빼면 다른 부분만 남는 다는 것을 착안
def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2
"""