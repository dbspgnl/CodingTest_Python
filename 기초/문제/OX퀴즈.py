def solution(quiz):
    answer = []
    for i in range(len(quiz)):
        quest = quiz[i].split(" = ")[0]
        ans = quiz[i].split(" = ")[1]
        answer.append("O" if eval(quest) == int(ans) else "X")
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))