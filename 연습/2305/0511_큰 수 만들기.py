# 주어진 숫자 문자열에서, k만큼 글자 수를 제거할 때, 최댓값
# 단, 순서를 지켜야 한다. (519,2) > 51 o / 95 x (스택)
def solution(number, k):
    stack = []
    for num in number:
        # 현재 수가 스택 마지막 값보다 크면
        while k > 0 and stack and stack[-1] < num: #
            stack.pop()
            k -= 1 # 처리 횟수
        stack.append(num)
    return "".join(stack[:len(stack)-k]) # stack 앞에서부터
print(solution("1924",2)) # 94
print(solution("1231234",3)) # 3234
print(solution("4177252841",4)) # 775841