def solution(s):
    answer = 0
    for i in range(len(s)): # 앞에서부터
        for j in range(len(s), i, -1): # 뒤에서부터
            new = s[i:j] # 범위 만큼
            reverse = new[::-1] # 그 범위의 역순
            if new == reverse: # 범위랑 역순이랑 같으면 = 팬린드롬
                answer = max(answer, len(new))
    return answer

print(solution("abcdcba")) # 7
print(solution("abacde")) # 3
