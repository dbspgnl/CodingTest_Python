def solution(s):
    stack = []
    for bracket in s:
        if bracket == "(":
            stack.append(bracket)
        else:
            if not stack: return False
            stack.pop()
    return len(stack) == 0 # 모두 비워지면 True

print(solution("()()")) # true
print(solution("(())()")) # true
print(solution(")()(")) # false
print(solution("(()(")) # false