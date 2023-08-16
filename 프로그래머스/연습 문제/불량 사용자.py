# 아이디 배열과 차단 아이디 배열이 주어질 때, 차단으로 인한 아이디 경우의 수
from itertools import permutations

def is_ban(user, banned_id):
    for i in range(len(banned_id)):
        if len(user[i]) != len(banned_id[i]): 
            return False # 애초에 길이가 다르면 해당안함
        for j in range(len(user[i])): # 글자 하나씩
            if banned_id[i][j] == "*":
                continue # 와일드 문자일 때는 넘어감
            if banned_id[i][j] != user[i][j]:
                return False # 글자가 다르면 해당안함
    return True # 모두 통과하면 밴에 해당함

def solution(user_id, banned_id):
    users = list(permutations(user_id, len(banned_id))) # 모든 순열 조합
    ban_list = []
    for user in users:
        if not is_ban(user, banned_id):
            continue
        else: # 밴 당한 유저
            user = set(user) # 중복 제거
            if user not in ban_list:
                ban_list.append(user)
    return len(ban_list)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) #2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) #2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) #3