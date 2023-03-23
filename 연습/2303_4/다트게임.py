# 숫자들을 모두 합한다.
# 숫자 다음에 나오는 S는 1승, D는 2승, T는 3승을 한다.
# *은 앞의 두 수를 곱하라. #은 앞의 수에 -1를 곱하라.

def solution(dartResult):
    scores = []
    start_idx = 0
    power = {'S':1, 'D':2, 'T':3}
    # 1. dartResult 파싱
    for i in range(len(dartResult)):
        op = dartResult[i]
        if op in power:
            scores.append(int(dartResult[start_idx:i]) ** power[op])
        elif op == "*":
            scores[-2:] = [ x * 2 for x in scores[-2:]]
        elif op == "#":
            scores[-1] = -scores[-1]
        if not op.isnumeric():
            start_idx = i+1
    # 2. 합을 반환
    return sum(scores)

print(solution('1S2D*3T'))