# words에 있는 단어만 허용하는 상태에서 begin에서 몇 번만에 target으로 변경할 수 있나?
from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0]) # 찾는 단어, depth(count)
    n = len(words)
    chk = [0]*n
    while q:
        word, cnt = q.popleft()
        if word == target: # 찾으면 종료
            answer = cnt
            break
        for i in range(n):
            temp = 0
            if not chk[i]: # 탐색 여부
                for j in range(len(word)): # 단어 내에서 탐색
                    if word[j] != words[i][j]: # 단어 배열과 얼마나 다른가
                        temp +=1
                if temp == 1: # 한 글자만 다를 경우
                    q.append([words[i], cnt+1])
                    chk[i] = 1 # 탐색 처리
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"])) # 0
# hit > cog : hit - hot - dot - dog - cog (4)