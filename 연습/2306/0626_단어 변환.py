# words에 있는 단어만 허용하는 상태에서 begin에서 몇 번만에 target으로 변경할 수 있나?
from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    n = len(words)
    chk = [0]*n
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(n): # 한 문자열씩 확인
            temp = 0
            if not chk[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp +=1
                if temp == 1:
                    q.append([words[i], cnt+1])
                    chk[i] = 1 # 방문 처리
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"])) # 0
# hit > cog : hit - hot - dot - dog - cog (4)