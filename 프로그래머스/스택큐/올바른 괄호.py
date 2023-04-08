def solution(s):
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack: # 스택이 없다면 종료
                return False
            stack.pop()
    return len(stack) == 0 # 마지막 pop까지 수행하고도 0이면 모두 수행함

print(solution("()()")) # true
print(solution("(())()")) # true
print(solution(")()(")) # false
print(solution("(()(")) # false