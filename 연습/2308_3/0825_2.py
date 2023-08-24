# 아이디 배열과 차단 아이디 배열이 주어질 때, 차단으로 인한 아이디 경우의 수
from itertools import permutations
def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id)))
    ban_set = []
    def check(users, banned_id):
        for i in range(len(banned_id)):
            if len(users[i]) != len(banned_id[i]): # 문자열 길이가 다르면 false
                return False
            for j in range(len(users[i])): # 하나씩 꺼내서 비교
                if banned_id[i][j] == "*":
                    continue
                if banned_id[i][j] != users[i][j]:
                    return False
        return True
    for users in user_permutation:
        if not check(users, banned_id):
            continue
        else:
            users = set(users)
            if users not in ban_set:
                ban_set.append(users)
    return len(ban_set)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) #2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) #2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) #3