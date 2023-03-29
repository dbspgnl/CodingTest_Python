def solution(s):
    array = s.split()
    i = 0
    while array:
        if len(array) <= i: break
        elif array[i] == "Z":
            array.remove(array[i])
            array.remove(array[i-1])
        else:
            i+=1
    return sum(map(int, array))

print(solution("1 2 Z 3")) # 4

"""
def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer
    
def solution(s):
    stack = []
    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                stack.pop()

    return sum(stack)
"""