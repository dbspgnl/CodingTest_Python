# words에 있는 단어만 허용하는 상태에서 begin에서 몇 번만에 target으로 변경할 수 있나?
from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin,0]) # 시작 단어, depth
    n = len(words)
    chk = [0]*n
    while q:
        word, cnt = q.popleft()
        if word == target: # 단어 찾으면 종료
            answer = cnt
            break
        for i in range(n):
            temp = 0
            if not chk[i]: # 탐색 여부
                for j in range(len(word)):
                    if word[j] != words[i][j]: # 탐색 중인 글자 수가 몇 글자나 다른가?
                        temp +=1
                if temp == 1: # 한 글자만 다를 경우
                    q.append([words[i], cnt+1])
                    chk[i] = 1 # 탐색 처리
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"])) # 0

# 사전형 방식으로 풀기
# from collections import deque
def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue
        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1
        if count == 1:
            yield word
def solution2(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])
    while queue:
        current = queue.popleft()
        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)
    return dist.get(target, 0)

print(solution2("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution2("hit","cog",["hot", "dot", "dog", "lot", "log"])) # 0