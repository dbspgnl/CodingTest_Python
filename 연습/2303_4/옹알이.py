def solution(babbling):
    can = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling:
        count = 0
        word = ""
        for j in i:
            word += j
            if word in can:
                word = ""
                count+=1
        if len(word) == 0 and count >0:
            answer +=1
    return answer
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))