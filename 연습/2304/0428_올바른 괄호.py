def solution(s):
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack: # 스택 없으면 실패
                return False
            stack.pop() # ")"가 들어왔으므로 한쌍인 "(" 처리
    return len(stack) == 0 # 모든 쌍이 존재하면 성공

print(solution("()()")) # true
print(solution("(())()")) # true
print(solution(")()(")) # false
print(solution("(()(")) # false